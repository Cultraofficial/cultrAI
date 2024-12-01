import os
from google.cloud import storage, aiplatform
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Your account-specific details
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

# Automatically set service account for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

def authenticate():
    """Authenticate with Google Cloud."""
    print("Authenticating with Google Cloud...")
    try:
        if not os.path.exists(SERVICE_ACCOUNT_FILE):
            raise FileNotFoundError(f"Service account file {SERVICE_ACCOUNT_FILE} not found.")
        print("Authentication successful!")
    except Exception as e:
        print(f"Authentication error: {e}")

def enable_apis():
    """Enable required APIs for the project."""
    print("Enabling APIs...")
    service = build("serviceusage", "v1")
    apis = [
        "aiplatform.googleapis.com",
        "bigquery.googleapis.com",
        "storage.googleapis.com",
        "compute.googleapis.com",
    ]
    for api in apis:
        try:
            request = service.services().enable(
                name=f"projects/{PROJECT_ID}/services/{api}"
            )
            response = request.execute()
            print(f"Enabled API {api}: {response}")
        except HttpError as e:
            print(f"Error enabling API {api}: {e}")

def create_storage_bucket():
    """Create a storage bucket for AI models."""
    print("Creating storage bucket...")
    try:
        storage_client = storage.Client()
        bucket = storage_client.create_bucket(BUCKET_NAME, location=REGION)
        print(f"Bucket {BUCKET_NAME} created successfully.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def upload_ai_models():
    """Download and upload AI models to Cloud Storage."""
    print("Uploading AI models...")
    for model in AI_MODELS:
        model_name = model.split("/")[-1]
        try:
            # Simulate model download
            print(f"Downloading model {model}...")
            model_path = f"/tmp/{model_name}.zip"
            with open(model_path, "w") as f:
                f.write(f"Mock data for {model_name}")

            # Upload to bucket
            storage_client = storage.Client()
            bucket = storage_client.bucket(BUCKET_NAME)
            blob = bucket.blob(f"models/{model_name}.zip")
            blob.upload_from_filename(model_path)
            print(f"Uploaded {model_name} to {BUCKET_NAME}.")
        except Exception as e:
            print(f"Error uploading model {model}: {e}")

def configure_billing():
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

def configure_budget():
    """Set up budget alerts for cost control."""
    print("Configuring budget...")
    try:
        billing_service = build("cloudbilling", "v1")
        budget_body = {
            "name": f"billingAccounts/{BILLING_ACCOUNT_ID}/budgets/{PROJECT_ID}",
            "budgetFilter": {"projects": [f"projects/{PROJECT_ID}"]},
            "amount": {"specifiedAmount": {"currencyCode": "USD", "units": "100"}},  # $100 budget
            "thresholdRules": [{"spendBasis": "CURRENT_SPEND", "thresholdPercent": 0.8}],
        }
        billing_service.billingAccounts().budgets().create(
            parent=f"billingAccounts/{BILLING_ACCOUNT_ID}", body=budget_body
        ).execute()
        print("Budget alerts configured successfully.")
    except HttpError as e:
        print(f"Error configuring budget: {e}")

def deploy_ai_pipeline():
    """Set up Vertex AI pipeline."""
    print("Setting up Vertex AI pipeline...")
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
    """Run the full automated setup."""
    print("Starting full automated setup for cultrAI...")
    authenticate()
    enable_apis()
    create_storage_bucket()
    upload_ai_models()
    configure_billing()
    configure_budget()
    deploy_ai_pipeline()
    print("Setup complete! Your platform is ready for use.")

if __name__ == "__main__":
    main()
