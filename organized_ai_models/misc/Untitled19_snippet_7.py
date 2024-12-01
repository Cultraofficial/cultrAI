from google.cloud import aiplatform
from google.cloud.resourcemanager_v3 import ProjectsClient
from google.cloud.exceptions import NotFound
import os
import sys

# Automatically configure credentials and project details
SERVICE_ACCOUNT_JSON = "/content/drive/My Drive/BrandNewKey.json"  # Update path if necessary
PROJECT_ID = "gen-lang-client-0492208227"  # Replace with your active project ID
REGION = "us-central1"

# Set up credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_JSON

def validate_project(project_id):
    try:
        client = ProjectsClient()
        project_name = f"projects/{project_id}"
        project = client.get_project(name=project_name)
        if project.state.name != "ACTIVE":
            print(f"Project {project_id} is not active. Current state: {project.state.name}")
            sys.exit(1)
        print(f"Project {project_id} is valid and active.")
    except NotFound:
        print(f"Error: Project {project_id} does not exist or has been deleted.")
        sys.exit(1)

def cleanup_vertex_ai_resources(project_id, region):
    try:
        aiplatform.init(project=project_id, location=region)

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
        sys.exit(1)

def disable_vertex_ai_api(project_id):
    try:
        client = ProjectsClient()
        project_name = f"projects/{project_id}"
        print("Disabling Vertex AI API...")
        client.delete_project(name=project_name)
        print("Vertex AI API disabled successfully!")
    except Exception as e:
        print(f"Error during API disable: {e}")
        sys.exit(1)

# Main Execution Flow
if __name__ == "__main__":
    print("Validating project...")
    validate_project(PROJECT_ID)

    print("Starting cleanup process...")
    cleanup_vertex_ai_resources(PROJECT_ID, REGION)

    print("Disabling Vertex AI API...")
    disable_vertex_ai_api(PROJECT_ID)
