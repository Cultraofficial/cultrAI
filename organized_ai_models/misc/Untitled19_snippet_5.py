from google.cloud import aiplatform
from google.cloud.resourcemanager import ProjectsClient
import os

# Automatically configure credentials and project details
SERVICE_ACCOUNT_JSON = "/content/drive/My Drive/BrandNewKey.json"
PROJECT_ID = "gen-lang-client-0492208227"  # Preconfigured project ID
REGION = "us-central1"

# Set up credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_JSON

def cleanup_vertex_ai_resources():
    try:
        # Initialize Vertex AI client
        aiplatform.init(project=PROJECT_ID, location=REGION)

        # Stop all Endpoints
        print("Stopping all active endpoints...")
        endpoints = aiplatform.Endpoint.list()
        for endpoint in endpoints:
            print(f"Deleting endpoint: {endpoint.display_name}")
            endpoint.delete()

        # Cancel all Training Pipelines
        print("Canceling all active training pipelines...")
        pipelines = aiplatform.PipelineJob.list()
        for pipeline in pipelines:
            if pipeline.state == "PIPELINE_STATE_RUNNING":
                print(f"Canceling pipeline: {pipeline.display_name}")
                pipeline.cancel()

        # Undeploy all Deployed Models
        print("Undeploying all deployed models...")
        endpoints = aiplatform.Endpoint.list()
        for endpoint in endpoints:
            deployed_models = endpoint.gca_resource.deployed_models
            for deployed_model in deployed_models:
                print(f"Undeploying model: {deployed_model.model}")
                endpoint.undeploy(deployed_model_id=deployed_model.id)

        print("All Vertex AI resources cleaned up successfully!")

    except Exception as e:
        print(f"Error during cleanup: {e}")

def disable_vertex_ai_api():
    try:
        # Initialize Resource Manager client
        client = ProjectsClient()

        # Disable Vertex AI API
        print("Disabling Vertex AI API...")
        project_name = f"projects/{PROJECT_ID}"
        client.delete_project(name=project_name)
        print("Vertex AI API disabled successfully!")

    except Exception as e:
        print(f"Error during API disable: {e}")


# Execute the cleanup
cleanup_vertex_ai_resources()

# Disable the Vertex AI API
disable_vertex_ai_api()
