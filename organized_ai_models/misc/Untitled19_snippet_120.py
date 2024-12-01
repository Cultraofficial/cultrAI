import os
from google.cloud import bigquery
from google.cloud import monitoring_dashboard_v1
from google.cloud import monitoring_v3
from google.cloud.exceptions import NotFound, Conflict

def setup_environment(project_id, json_key_path):
    try:
        # Step 1: Authenticate with the service account JSON
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key_path

        # Step 2: Initialize Clients
        bq_client = bigquery.Client()
        dashboard_client = monitoring_dashboard_v1.DashboardsServiceClient()
        monitoring_client = monitoring_v3.MetricServiceClient()

        # Step 3: Create BigQuery Dataset and Table
        print("Setting up BigQuery dataset and table for billing export...")
        dataset_id = "billing_export"
        table_id = "gcp_billing_export"
        dataset_ref = bigquery.Dataset(f"{project_id}.{dataset_id}")

        try:
            dataset = bq_client.get_dataset(dataset_ref)
            print(f"Dataset '{dataset_id}' already exists.")
        except NotFound:
            dataset = bigquery.Dataset(dataset_ref)
            dataset.location = "US"
            dataset = bq_client.create_dataset(dataset)
            print(f"Dataset '{dataset_id}' created successfully.")

        table_ref = dataset_ref.table(table_id)
        try:
            table = bq_client.get_table(table_ref)
            print(f"Table '{table_id}' already exists.")
        except NotFound:
            schema = [
                bigquery.SchemaField("billing_account_id", "STRING", mode="REQUIRED"),
                bigquery.SchemaField("service", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("cost", "FLOAT", mode="NULLABLE"),
                bigquery.SchemaField("currency", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("usage_start_time", "TIMESTAMP", mode="NULLABLE"),
                bigquery.SchemaField("usage_end_time", "TIMESTAMP", mode="NULLABLE"),
            ]
            table = bigquery.Table(table_ref, schema=schema)
            table = bq_client.create_table(table)
            print(f"Table '{table_id}' created successfully.")

        # Step 4: Enable Billing Export
        print("Enabling billing export...")
        # Unfortunately, enabling billing export must be done through the Cloud Console
        # or via an API request (not supported directly via Python).
        print("Please ensure billing export is enabled for the BigQuery table.")

        # Step 5: Create Cloud Monitoring Dashboard
        print("Creating monitoring dashboard...")
        parent = f"projects/{project_id}"
        dashboard = {
            "display_name": "Cloud Billing Dashboard",
            "grid_layout": {
                "columns": 2,
                "widgets": [
                    {
                        "title": "Billing Costs",
                        "xy_chart": {
                            "data_sets": [
                                {
                                    "time_series_query": {
                                        "time_series_filter": {
                                            "filter": 'metric.type="billing.gcp.cumulative_cost"',
                                            "aggregation": {
                                                "alignment_period": "3600s",
                                                "per_series_aligner": "ALIGN_SUM",
                                            },
                                        }
                                    },
                                    "target_axis": "Y1",
                                }
                            ],
                        },
                    }
                ],
            },
        }

        try:
            response = dashboard_client.create_dashboard(parent=parent, dashboard=dashboard)
            print(f"Dashboard created successfully: {response.name}")
        except Conflict:
            print("Dashboard already exists.")

        print("Setup complete!")

    except Exception as e:
        print(f"Error occurred during setup: {e}")


# Replace these values with your actual project ID and JSON key file path
project_id = "gen-lang-client-0492208227"
json_key_path = "/content/drive/My Drive/BrandNewKey.json"

setup_environment(project_id, json_key_path)
