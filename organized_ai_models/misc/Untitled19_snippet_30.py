import os
import time
from google.cloud import storage, aiplatform
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Account details
PROJECT_ID = "cultrai"
BILLING_ACCOUNT_ID = "0135D3-D70314-042927"
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/BrandNewKey.json"
BUCKET_NAME = f"{PROJECT_ID}-models-bucket"
REGION = "us-central1"
AI_MODELS = [
    "EleutherAI/gpt-neo-2.7B",
    "huggingface/transformers",
    "mistralai/Mistral-7B",
    "google/bert-base-uncased",
    "facebook/bart-large",
]

# Environment setup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

def authenticate():
    """Authenticate with Google Cloud."""
    print("Authenticating with Google Cloud...")
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        raise FileNotFoundError(f"Service account file {SERVICE_ACCOUNT_FILE} not found.")
    print("Authentication successful!")

def enable_api(service_name):
    """Enable a single API for the project."""
    print(f"Enabling API: {service_name}...")
    try:
        service = build("serviceusage", "v1")
        request = service.services().enable(
            name=f"projects/{PROJECT_ID}/services/{service_name}"
        )
        response = request.execute()
        print(f"Enabled API: {service_name}")
        return response
    except HttpError as e:
        print(f"Error enabling API {service_name}: {e}")
        return None

def enable_apis():
    """Enable all required APIs for the project."""
    print("Enabling required APIs...")
    apis = [
        "aiplatform.googleapis.com",
        "bigquery.googleapis.com",
        "storage.googleapis.com",
        "compute.googleapis.com",
    ]
    for api in apis:
        enable_api(api)

def create_storage_bucket():
    """Create a Cloud Storage bucket."""
    print(f"Creating storage bucket: {BUCKET_NAME}...")
    try:
        storage_client = storage.Client()
        bucket = storage_client.create_bucket(BUCKET_NAME, location=REGION)
        print(f"Bucket {BUCKET_NAME} created successfully.")
        return bucket
    except HttpError as e:
        if "already exists" in str(e):
            print(f"Bucket {BUCKET_NAME} already exists. Skipping creation.")
        else:
            print(f"Error creating bucket: {e}")

def upload_ai_models():
    """Upload AI models to Cloud Storage."""
    print("Uploading AI models to bucket...")
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    for model in AI_MODELS:
        model_name = model.split("/")[-1]
        print(f"Uploading model: {model_name}")
        try:
            blob = bucket.blob(f"models/{model_name}.zip")
            # Simulating local model file
            model_path = f"/tmp/{model_name}.zip"
            with open(model_path, "w") as f:
                f.write("Simulated model content")
            blob.upload_from_filename(model_path)
            print(f"Uploaded model {model_name} to {BUCKET_NAME}")
        except Exception as e:
            print(f"Error uploading model {model_name}: {e}")

def link_billing_account():
    """Link the billing account to the project."""
    print("Linking billing account...")
    try:
        billing_service = build("cloudbilling", "v1")
        billing_info = {
            "name": f"projects/{PROJECT_ID}/billingInfo",
            "projectId": PROJECT_ID,
            "billingAccountName": f"billingAccounts/{BILLING_ACCOUNT_ID}",
            "billingEnabled": True,
        }
        billing_service.projects().updateBillingInfo(name=f"projects/{PROJECT_ID}", body=billing_info).execute()
        print(f"Billing account {BILLING_ACCOUNT_ID} linked successfully.")
    except HttpError as e:
        print(f"Error linking billing account: {e}")

def retry(func, retries=3, delay=5):
    """Retry a function in case of failure."""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    print(f"All attempts to execute {func.__name__} failed.")

def deploy_vertex_ai_pipeline():
    """Deploy a Vertex AI pipeline."""
    print("Deploying Vertex AI pipeline...")
    try:
        aiplatform.init(project=PROJECT_ID, location=REGION)
        pipeline_job = aiplatform.PipelineJob(
            display_name="cultrAI-pipeline",
            template_path="gs://google-cloud-aiplatform/templates/training_pipeline.json",
            parameter_values={"model_name": "cultrAI-Model"},
        )
        pipeline_job.run(sync=True)
        print("Vertex AI pipeline deployed successfully.")
    except Exception as e:
        print(f"Error deploying Vertex AI pipeline: {e}")

def main():
    """Main function to execute the full setup."""
    print("Starting enhanced automated setup for cultrAI...")
    retry(authenticate)
    retry(enable_apis)
    retry(create_storage_bucket)
    retry(upload_ai_models)
    retry(link_billing_account)
    retry(deploy_vertex_ai_pipeline)
    print("Enhanced setup completed successfully!")

if __name__ == "__main__":
    main()
