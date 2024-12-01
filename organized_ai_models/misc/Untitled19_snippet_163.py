import os
import time
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# CONFIGURE PROJECT DETAILS
PROJECT_ID = "neo-project"  # Unique project ID
BILLING_ACCOUNT_ID = "6615-5644-0251-0280"  # Replace with your billing account ID
SERVICE_ACCOUNT_KEY_PATH = "path/to/neo-key.json"  # Path to the service account JSON key

# List of APIs to enable
REQUIRED_APIS = [
    "aiplatform.googleapis.com",
    "bigquery.googleapis.com",
    "storage.googleapis.com",
    "compute.googleapis.com",
]

def authenticate():
    """Authenticate using the service account key."""
    try:
        print("🔒 Authenticating...")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY_PATH
        credentials, _ = google.auth.default()
        print("✅ Authentication successful!")
        return credentials
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        return None

def create_project():
    """Create a new Google Cloud project."""
    try:
        print("✨ Creating new Google Cloud project...")
        service = build("cloudresourcemanager", "v1")
        request = service.projects().create(body={"projectId": PROJECT_ID, "name": PROJECT_ID})
        response = request.execute()
        print(f"✅ Project created successfully: {response['projectId']}")
    except HttpError as e:
        print(f"❌ Failed to create project: {e}")

def enable_apis():
    """Enable necessary APIs."""
    print("🔮 Enabling required APIs...")
    for api in REQUIRED_APIS:
        try:
            print(f"🔮 Enabling API: {api}...")
            service = build("serviceusage", "v1")
            request = service.services().enable(name=f"projects/{PROJECT_ID}/services/{api}")
            response = request.execute()
            print(f"✅ API enabled: {api}")
        except HttpError as e:
            print(f"❌ Failed to enable API {api}: {e}")

def create_bucket():
    """Create a storage bucket."""
    try:
        print("✨ Creating storage bucket...")
        storage_client = build("storage", "v1")
        bucket_body = {
            "name": f"{PROJECT_ID}-bucket",
            "location": "US",
        }
        request = storage_client.buckets().insert(project=PROJECT_ID, body=bucket_body)
        response = request.execute()
        print(f"✅ Bucket created: {response['name']}")
        return response["name"]
    except HttpError as e:
        print(f"❌ Failed to create bucket: {e}")
        return None

def upload_model(bucket_name, model_name, file_path):
    """Upload a model to the storage bucket."""
    try:
        print(f"📦 Uploading model: {model_name}...")
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
        print("💳 Linking billing account...")
        service = build("cloudbilling", "v1")
        request = service.projects().updateBillingInfo(
            name=f"projects/{PROJECT_ID}",
            body={"billingAccountName": f"billingAccounts/{BILLING_ACCOUNT_ID}"},
        )
        response = request.execute()
        print(f"✅ Billing linked successfully!")
    except HttpError as e:
        print(f"❌ Failed to link billing account: {e}")

def cheat_code_retry(function, *args, retries=3, delay=2):
    """Retry a function multiple times with a delay in case of failure."""
    for attempt in range(1, retries + 1):
        try:
            return function(*args)
        except Exception as e:
            print(f"⚠️ Attempt {attempt} failed: {e}")
            time.sleep(delay)
    print(f"❌ All attempts failed for {function.__name__}.")

def main():
    print("🧠 Welcome to the Neo Setup!")
    credentials = authenticate()
    if not credentials:
        return

    # Create project with retry mechanism
    cheat_code_retry(create_project)

    # Enable required APIs
    enable_apis()

    # Create a storage bucket
    bucket_name = cheat_code_retry(create_bucket)
    if not bucket_name:
        print("❌ Storage bucket creation failed. Exiting setup.")
        return

    # Upload AI models
    models = {
        "gpt-neo-2.7B": "path/to/gpt-neo-2.7B",
        "transformers": "path/to/transformers",
        "mistral-7B": "path/to/mistral-7B",
    }
    for model_name, file_path in models.items():
        cheat_code_retry(upload_model, bucket_name, model_name, file_path)

    # Link billing account
    cheat_code_retry(link_billing)

    print("🎉 Neo Setup completed successfully! The Matrix is ready.")

if __name__ == "__main__":
    main()
