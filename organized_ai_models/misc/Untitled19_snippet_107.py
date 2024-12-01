from google.cloud import bigquery, billing_v1
from google.api_core.exceptions import NotFound, Forbidden
from google.cloud.exceptions import GoogleCloudError
import os
from datetime import datetime, timedelta


def enable_bigquery_billing_export_and_analyze():
    try:
        # Define project and billing account
        project_id = "gen-lang-client-0492208227"
        billing_account = "billingAccounts/0135D3-D70314-042927"
        dataset_id = "billing_export"
        table_id = "gcp_billing_export_v1"

        # Step 1: Enable BigQuery billing export
        print("Enabling BigQuery billing export...")
        billing_client = billing_v1.CloudBillingClient()
        project_name = f"projects/{project_id}"
        billing_client.update_project_billing_info(
            name=project_name,
            project_billing_info={"billing_account_name": billing_account}
        )
        print(f"BigQuery billing export enabled for project: {project_id}")

        # Step 2: Check if dataset exists, if not create it
        print("Checking BigQuery dataset and table...")
        bq_client = bigquery.Client(project=project_id)
        dataset_ref = f"{project_id}.{dataset_id}"
        try:
            bq_client.get_dataset(dataset_ref)
            print(f"Dataset '{dataset_id}' already exists.")
        except NotFound:
            print(f"Dataset '{dataset_id}' not found. Creating...")
            dataset = bigquery.Dataset(dataset_ref)
            dataset.location = "US"
            bq_client.create_dataset(dataset)
            print(f"Dataset '{dataset_id}' created successfully.")

        # Step 3: Query billing data
        print("Querying BigQuery billing data...")
        start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        end_date = datetime.now().strftime("%Y-%m-%d")

        query = f"""
            SELECT
                service.description AS service,
                SUM(cost) AS total_cost
            FROM `{project_id}.{dataset_id}.{table_id}`
            WHERE usage_start_time BETWEEN TIMESTAMP("{start_date}") AND TIMESTAMP("{end_date}")
            GROUP BY service
            ORDER BY total_cost DESC
        """
        try:
            query_job = bq_client.query(query)
            print("Billing Data Analysis Results:")
            for row in query_job:
                print(f"Service: {row['service']}, Total Cost: ${row['total_cost']:.2f}")
        except NotFound:
            print(f"Table '{table_id}' not found in dataset '{dataset_id}'. Ensure billing export is configured.")
        except Forbidden:
            print("Access to BigQuery billing data is forbidden. Check permissions for the service account.")

    except GoogleCloudError as e:
        print(f"Error during BigQuery billing export enablement and analysis: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


# Run the function
enable_bigquery_billing_export_and_analyze()
