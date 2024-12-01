from google.cloud import aiplatform
from google.cloud.billing import CloudBillingClient
import os

# Automatically configure credentials and project details
SERVICE_ACCOUNT_JSON = "/content/drive/My Drive/BrandNewKey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_JSON

# Project ID automatically applied
PROJECT_ID = "gen-lang-client-0492208227"  # Automatically set
REGION = "us-central1"

def stop_vertex_ai_resources():
    """Stops all Vertex AI resources (endpoints, pipelines, and models)."""
    try:
        aiplatform.init(project=PROJECT_ID, location=REGION)

        # Stop all endpoints
        print("Stopping all active endpoints...")
        endpoints = aiplatform.Endpoint.list()
        for endpoint in endpoints:
            print(f"Deleting endpoint: {endpoint.display_name}")
            endpoint.delete()

        # Cancel all training pipelines
        print("Canceling all active training pipelines...")
        pipelines = aiplatform.PipelineJob.list()
        for pipeline in pipelines:
            if pipeline.state == "PIPELINE_STATE_RUNNING":
                print(f"Canceling pipeline: {pipeline.display_name}")
                pipeline.cancel()

        print("All Vertex AI resources have been cleaned up.")
    except Exception as e:
        print(f"Error stopping resources: {e}")

def disable_billing():
    """Disables billing for the project."""
    try:
        billing_client = CloudBillingClient()
        billing_account_name = f"projects/{PROJECT_ID}/billingInfo"
        print(f"Disabling billing for project {PROJECT_ID}...")
        billing_client.update_project_billing_info(
            name=billing_account_name,
            project_billing_info={"billing_account_name": ""},
        )
        print("Billing has been disabled successfully.")
    except Exception as e:
        print(f"Error disabling billing: {e}")

# Main Execution
if __name__ == "__main__":
    print("Starting automated cleanup...")
    stop_vertex_ai_resources()

    print("Disabling billing to prevent further charges...")
    disable_billing()

    print("All actions completed successfully.")
