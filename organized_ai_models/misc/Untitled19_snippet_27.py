import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Automatically apply the project details
PROJECT_NAME = "cultrAI"
PROJECT_ID = "cultrai"
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/BrandNewKey.json"

# Set up Google Cloud environment variables
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

def enable_apis(project_id):
    """Enable necessary APIs for the project."""
    try:
        print(f"Enabling APIs for project: {project_id}...")
        service_usage = build("serviceusage", "v1")
        apis_to_enable = [
            "aiplatform.googleapis.com",  # Vertex AI
            "cloudresourcemanager.googleapis.com",  # Resource Manager
            "cloudbilling.googleapis.com",  # Billing API
            "storage.googleapis.com",  # Cloud Storage
            "iam.googleapis.com",  # IAM API
        ]
        for api in apis_to_enable:
            print(f"Enabling {api}...")
            request = service_usage.services().enable(
                name=f"projects/{project_id}/services/{api}"
            )
            request.execute()
        print("✅ All APIs enabled successfully!")
    except HttpError as e:
        print(f"Error enabling APIs: {e}")

def create_bucket(project_id):
    """Create a Cloud Storage bucket."""
    try:
        print(f"Creating a Cloud Storage bucket for project: {project_id}...")
        storage_client = build("storage", "v1")
        bucket_name = f"{project_id}-bucket"
        bucket_body = {
            "name": bucket_name,
            "location": "US",
        }
        request = storage_client.buckets().insert(
            project=project_id, body=bucket_body
        )
        request.execute()
        print(f"✅ Bucket '{bucket_name}' created successfully!")
    except HttpError as e:
        print(f"Error creating bucket: {e}")

def validate_project(project_id):
    """Validate the project to ensure it's ready for use."""
    try:
        print(f"Validating project: {project_id}...")
        crm_service = build("cloudresourcemanager", "v1")
        request = crm_service.projects().get(projectId=project_id)
        response = request.execute()
        print(f"✅ Project '{response['name']}' (ID: {response['projectId']}) is active.")
    except HttpError as e:
        print(f"Error validating project: {e}")

def setup_project():
    """Automate the complete setup for the project."""
    print(f"Starting setup for project: {PROJECT_NAME} (ID: {PROJECT_ID})...")
    validate_project(PROJECT_ID)
    enable_apis(PROJECT_ID)
    create_bucket(PROJECT_ID)
    print("\n✅ Setup completed successfully! Your project is ready for use.")

# Execute the setup
if __name__ == "__main__":
    setup_project()
