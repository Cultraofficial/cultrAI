from google.cloud import bigquery, monitoring_v3, billing_v1, logging_v2
from google.cloud import resourcemanager_v3
from google.auth.exceptions import DefaultCredentialsError
from google.api_core.exceptions import GoogleAPIError
import os


def auto_configure_gcp():
    """
    A fully automated script that configures GCP with all necessary setups
    for billing, BigQuery, monitoring, and IAM, using project details from context.
    """

    try:
        # Set service account JSON dynamically from previous setup
        json_key_path = "/content/BrandNewKey.json"
        if not os.path.exists(json_key_path):
            raise FileNotFoundError(f"Service account key not found at {json_key_path}")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key_path
        print(f"Service account JSON loaded from {json_key_path}")

        # Automatically apply project details
        project_id = "gen-lang-client-0492208227"
        billing_account_name = "billingAccounts/0135D3-D70314-042927"

        # Authenticate and validate billing
        billing_client = billing_v1.CloudBillingClient()
        billing_info = billing_client.get_project_billing_info(name=f"projects/{project_id}")
        if not billing_info.billing_enabled:
            print("Enabling billing...")
            billing_client.update_project_billing_info(
                name=f"projects/{project_id}",
                project_billing_info={
                    "billing_account_name": billing_account_name,
                    "billing_enabled": True,
                },
            )
            print("Billing enabled successfully.")
        else:
            print("Billing is already enabled.")

        # Ensure BigQuery dataset and table exist
        bigquery_client = bigquery.Client()
        dataset_id = "billing_export"
        table_id = "gcp_billing_export"

        dataset_ref = bigquery_client.dataset(dataset_id)
        try:
            dataset = bigquery_client.get_dataset(dataset_ref)
            print(f"Dataset '{dataset_id}' exists.")
        except GoogleAPIError:
            print(f"Creating dataset '{dataset_id}'...")
            dataset = bigquery.Dataset(dataset_ref)
            dataset.location = "US"
            bigquery_client.create_dataset(dataset)
            print(f"Dataset '{dataset_id}' created successfully.")

        table_ref = dataset_ref.table(table_id)
        try:
            table = bigquery_client.get_table(table_ref)
            print(f"Table '{table_id}' exists.")
        except GoogleAPIError:
            print(f"Creating table '{table_id}'...")
            schema = [
                bigquery.SchemaField("timestamp", "TIMESTAMP"),
                bigquery.SchemaField("cost", "FLOAT"),
                bigquery.SchemaField("service", "STRING"),
            ]
            table = bigquery.Table(table_ref, schema=schema)
            bigquery_client.create_table(table)
            print(f"Table '{table_id}' created successfully.")

        # Ensure monitoring dashboard exists
        dashboard_client = monitoring_v3.DashboardsServiceClient()
        project_name = f"projects/{project_id}"
        dashboard_name = "Cost Monitoring Dashboard"

        try:
            dashboards = list(dashboard_client.list_dashboards(parent=project_name))
            if not any(dashboard.display_name == dashboard_name for dashboard in dashboards):
                print("Creating monitoring dashboard...")
                dashboard = monitoring_v3.Dashboard(
                    display_name=dashboard_name,
                    grid_layout=monitoring_v3.GridLayout(
                        columns=2,
                        widgets=[
                            monitoring_v3.Widget(
                                title="GCP Cost",
                                scorecard=monitoring_v3.Scorecard(
                                    time_series_query=monitoring_v3.TimeSeriesQuery(
                                        prometheus_query="rate(cost[5m])"
                                    )
                                ),
                            )
                        ],
                    ),
                )
                dashboard_client.create_dashboard(parent=project_name, dashboard=dashboard)
                print(f"Dashboard '{dashboard_name}' created successfully.")
            else:
                print("Monitoring dashboard already exists.")
        except GoogleAPIError as e:
            print(f"Failed to create monitoring dashboard: {e}")

        # Ensure required IAM roles are assigned
        resourcemanager_client = resourcemanager_v3.ProjectsClient()
        iam_policy = resourcemanager_client.get_iam_policy(resource=project_id)
        required_roles = [
            "roles/bigquery.dataEditor",
            "roles/bigquery.jobUser",
            "roles/monitoring.editor",
            "roles/iam.serviceAccountUser",
        ]
        current_roles = [binding.role for binding in iam_policy.bindings]
        missing_roles = [role for role in required_roles if role not in current_roles]

        if missing_roles:
            print(f"Adding missing IAM roles: {missing_roles}")
            for role in missing_roles:
                iam_policy.bindings.add(role=role)
            resourcemanager_client.set_iam_policy(resource=project_id, policy=iam_policy)
            print("IAM roles updated successfully.")
        else:
            print("All required IAM roles are already assigned.")

        print("All configurations have been validated and fixed!")

    except DefaultCredentialsError:
        print("Failed to authenticate. Ensure the service account JSON is properly set up.")
    except Exception as e:
        print(f"An error occurred during configuration: {e}")


# Execute the auto-configuration
if __name__ == "__main__":
    auto_configure_gcp()
