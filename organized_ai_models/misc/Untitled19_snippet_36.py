import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import time

# Configuration
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/BrandNewKey.json"
PROJECT_ID = "cultrai-new"
NEW_BUCKET_NAME = f"{PROJECT_ID}-bucket"
BILLING_ACCOUNT_ID = "6615-5644-0251-0280"
MODELS = ["EleutherAI/gpt-neo-2.7B", "huggingface/transformers", "mistralai/Mistral-7B"]

def authenticate():
    print("🔒 Authenticating...")
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    print("✅ Authentication successful!")
    return credentials

def create_project(credentials):
    print("✨ Creating new Google Cloud project...")
    try:
        service = build("cloudresourcemanager", "v1", credentials=credentials)
        project_body = {"project_id": PROJECT_ID, "name": PROJECT_ID}
        request = service.projects().create(body=project_body)
        request.execute()
        print(f"✅ Project '{PROJECT_ID}' created successfully!")
    except Exception as e:
        print(f"❌ Failed to create project: {e}")

def enable_api(api_name, credentials):
    print(f"🔮 Enabling API: {api_name}...")
    try:
        service = build("serviceusage", "v1", credentials=credentials)
        request = service.services().enable(
            name=f"projects/{PROJECT_ID}/services/{api_name}"
        )
        request.execute()
        print(f"✅ API {api_name} enabled successfully!")
    except Exception as e:
        print(f"❌ Failed to enable API {api_name}: {e}")

def create_bucket(bucket_name, credentials):
    print(f"✨ Creating storage bucket: {bucket_name}...")
    try:
        service = build("storage", "v1", credentials=credentials)
        bucket_body = {"name": bucket_name}
        request = service.buckets().insert(project=PROJECT_ID, body=bucket_body)
        request.execute()
        print(f"✅ Bucket '{bucket_name}' created successfully!")
    except Exception as e:
        print(f"❌ Failed to create bucket: {e}")

def upload_model(bucket_name, model_name, credentials):
    print(f"📦 Uploading model: {model_name}...")
    try:
        service = build("storage", "v1", credentials=credentials)
        blob_name = model_name.split("/")[-1] + ".bin"
        media = {"name": blob_name}
        request = service.objects().insert(bucket=bucket_name, body=media)
        request.execute()
        print(f"✅ Model '{model_name}' uploaded successfully!")
    except Exception as e:
        print(f"❌ Failed to upload model {model_name}: {e}")

def link_billing(credentials):
    print("💳 Linking billing account...")
    try:
        service = build("cloudbilling", "v1", credentials=credentials)
        billing_body = {"billingAccountName": BILLING_ACCOUNT_ID}
        request = service.projects().updateBillingInfo(
            name=f"projects/{PROJECT_ID}", body=billing_body
        )
        request.execute()
        print("✅ Billing account linked successfully!")
    except Exception as e:
        print(f"❌ Failed to link billing account: {e}")

def main():
    credentials = authenticate()

    # Step 1: Create a new project
    create_project(credentials)

    # Step 2: Enable necessary APIs
    apis = [
        "aiplatform.googleapis.com",
        "bigquery.googleapis.com",
        "storage.googleapis.com",
        "compute.googleapis.com",
    ]
    for api in apis:
        enable_api(api, credentials)

    # Step 3: Create a storage bucket
    create_bucket(NEW_BUCKET_NAME, credentials)

    # Step 4: Upload models to bucket
    for model in MODELS:
        upload_model(NEW_BUCKET_NAME, model, credentials)

    # Step 5: Link billing account
    link_billing(credentials)

    print("🚀 Adaptive setup completed successfully!")

if __name__ == "__main__":
    main()
