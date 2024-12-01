import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# CONFIGURE YOUR PROJECT DETAILS
PROJECT_ID = "cultrai-future"  # Use a unique name for the new project
BILLING_ACCOUNT_ID = "your-billing-account-id"  # Replace with valid billing account
SERVICE_ACCOUNT_KEY_PATH = "path/to/new-key.json"  # Replace with new service account key

def authenticate():
    """Authenticate using the service account key."""
    try:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY_PATH
        credentials, _ = google.auth.default()
        return credentials
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        return None

def create_project():
    """Create a new Google Cloud project."""
    try:
        service = build("cloudresourcemanager", "v1")
        request = service.projects().create(body={"projectId": PROJECT_ID, "name": PROJECT_ID})
        response = request.execute()
        print(f"✅ Project created successfully: {response['projectId']}")
    except HttpError as e:
        print(f"❌ Failed to create project: {e}")

def enable_apis():
    """Enable necessary APIs."""
    apis = [
        "aiplatform.googleapis.com",
        "bigquery.googleapis.com",
        "storage.googleapis.com",
        "compute.googleapis.com",
    ]
    for api in apis:
        try:
            service = build("serviceusage", "v1")
            request = service.services().enable(name=f"projects/{PROJECT_ID}/services/{api}")
            response = request.execute()
            print(f"✅ API enabled: {api}")
        except HttpError as e:
            print(f"❌ Failed to enable API {api}: {e}")

def create_bucket():
    """Create a storage bucket."""
    try:
        storage_client = build("storage", "v1")
        bucket_body = {
            "name": f"{PROJECT_ID}-bucket",
            "location": "US",
        }
        request = storage_client.buckets().insert(project=PROJECT_ID, body=bucket_body)
        response = request.execute()
        print(f"✅ Bucket created: {response['name']}")
    except HttpError as e:
        print(f"❌ Failed to create bucket: {e}")

def upload_model(bucket_name, model_name, file_path):
    """Upload a model to the storage bucket."""
    try:
        storage_client = build("storage", "v1")
        with open(file_path, "rb") as f:
            request = storage_client.objects().insert(
                bucket=bucket_name,
                name=model_name,
                media_body=f,
            )
            response = request.execute()
            print(f"✅ Model uploaded: {model_name}")
    except HttpError as e:
        print(f"❌ Failed to upload model {model_name}: {e}")

def link_billing():
    """Link a billing account to the project."""
    try:
        service = build("cloudbilling", "v1")
        request = service.projects().updateBillingInfo(
            name=f"projects/{PROJECT_ID}",
            body={"billingAccountName": f"billingAccounts/{BILLING_ACCOUNT_ID}"},
        )
        response = request.execute()
        print(f"✅ Billing linked: {response}")
    except HttpError as e:
        print(f"❌ Failed to link billing account: {e}")

def main():
    print("🔒 Authenticating...")
    credentials = authenticate()
    if not credentials:
        return

    print("✨ Creating new Google Cloud project...")
    create_project()

    print("🔮 Enabling required APIs...")
    enable_apis()

    print("✨ Creating storage bucket...")
    create_bucket()

    print("📦 Uploading models...")
    bucket_name = f"{PROJECT_ID}-bucket"
    models = {
        "gpt-neo-2.7B": "path/to/gpt-neo-2.7B",
        "transformers": "path/to/transformers",
    }
    for model_name, file_path in models.items():
        upload_model(bucket_name, model_name, file_path)

    print("💳 Linking billing account...")
    link_billing()

    print("🎉 Setup completed successfully!")

if __name__ == "__main__":
    main()
