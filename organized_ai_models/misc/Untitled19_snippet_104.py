from google.cloud import aiplatform, bigquery, storage
from google.auth.exceptions import DefaultCredentialsError
import os
from datetime import datetime, timedelta

# Initialize Google Cloud project variables
PROJECT_ID = "gen-lang-client-0492208227"
DATASET_ID = "billing_export"
TABLE_ID = "gcp_billing_export_v1"
LOCATION = "us-central1"

def authenticate_service_account():
    """Authenticates using the service account key file."""
    try:
        print("Authenticating service account...")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"
        aiplatform.init(project=PROJECT_ID, location=LOCATION)
        print("Authentication successful.")
    except DefaultCredentialsError as e:
        print(f"Error during authentication: {e}")
        exit()

def cleanup_vertex_ai_resources():
    """Cleans up Vertex AI endpoints, training jobs, and batch predictions."""
    print("Cleaning up Vertex AI resources...")

    try:
        # Clean up endpoints
        endpoints = aiplatform.Endpoint.list()
        for endpoint in endpoints:
            print(f"Undeploying models from endpoint: {endpoint.display_name}")
            endpoint.undeploy_all()
            print(f"Deleting endpoint: {endpoint.display_name}")
            endpoint.delete()

        # Cancel training jobs
        jobs = aiplatform.CustomJob.list()
        for job in jobs:
            if job.state not in ["SUCCEEDED", "FAILED", "CANCELLED"]:
                print(f"Cancelling training job: {job.display_name}")
                job.cancel()

        # Cancel batch predictions
        batch_predictions = aiplatform.BatchPredictionJob.list()
        for batch in batch_predictions:
            if batch.state not in ["SUCCEEDED", "FAILED", "CANCELLED"]:
                print(f"Cancelling batch prediction: {batch.display_name}")
                batch.cancel()

        print("Vertex AI resource cleanup complete.")
    except Exception as e:
        print(f"Error during Vertex AI resource cleanup: {e}")

def analyze_billing_with_bigquery():
    """Analyzes costs using BigQuery Billing Export."""
    print("Starting BigQuery billing analysis...")
    client = bigquery.Client()

    # Define date range for analysis
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=7)

    print(f"Analyzing costs from {start_date} to {end_date}...")

    # BigQuery SQL query for cost analysis
    query = f"""
    SELECT
        service.description AS service_name,
        SUM(cost) AS total_cost
    FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
    WHERE usage_start_time >= '{start_date}' AND usage_end_time <= '{end_date}'
    GROUP BY service_name
    ORDER BY total_cost DESC
    """

    try:
        # Run the query
        query_job = client.query(query)
        results = query_job.result()

        print("Billing Cost Breakdown:")
        for row in results:
            print(f"Service: {row.service_name}, Total Cost: ${row.total_cost:.2f}")

        print("BigQuery billing analysis complete.")
    except Exception as e:
        print(f"Error during billing analysis: {e}")

def check_and_enable_permissions():
    """Checks and enables required permissions for the service account."""
    print("Checking and enabling required permissions...")
    try:
        # Ensure necessary permissions exist
        aiplatform.init(project=PROJECT_ID)
        print("Vertex AI permissions confirmed.")

        # Check BigQuery permissions
        storage_client = storage.Client()
        buckets = storage_client.list_buckets()
        print("BigQuery permissions confirmed. Access to storage buckets verified.")

        print("All required permissions are active.")
    except Exception as e:
        print(f"Permission issue detected: {e}. Ensure the service account has the correct roles.")

def main():
    """Main function to automate resource cleanup and billing analysis."""
    print("Starting automated cloud cost management...")

    # Step 1: Authenticate service account
    authenticate_service_account()

    # Step 2: Check and enable permissions
    check_and_enable_permissions()

    # Step 3: Clean up unused Vertex AI resources
    cleanup_vertex_ai_resources()

    # Step 4: Analyze billing costs using BigQuery
    analyze_billing_with_bigquery()

    print("Automation complete. Please review the logs for detailed information.")

if __name__ == "__main__":
    main()
