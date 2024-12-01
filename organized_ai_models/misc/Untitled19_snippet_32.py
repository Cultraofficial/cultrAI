import os
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime
import time

# Configurations
SERVICE_ACCOUNT_FILE = "My Drive/BrandNewKey.json"  # Path to service account JSON file
PROJECT_ID = "cultrai"
BILLING_ACCOUNT_ID = "billingAccounts/6615-5644-0251-0280"
BUCKET_NAME = f"{PROJECT_ID}-magic-bucket"
AI_MODELS = [
    "EleutherAI/gpt-neo-2.7B",
    "huggingface/transformers",
    "mistralai/Mistral-7B",
    "google/bert-base-uncased",
    "facebook/bart-large",
]

# Helper Functions
def authenticate_service():
    print("🔓 Authenticating...")
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    return credentials

def enable_api(service_name, project_id, credentials):
    print(f"🔮 Enabling API: {service_name}...")
    try:
        service = build("serviceusage", "v1", credentials=credentials)
        request = service.services().enable(name=f"projects/{project_id}/services/{service_name}")
        request.execute()
        print(f"✅ API {service_name} enabled successfully!")
    except Exception as e:
        print(f"❌ Couldn't enable API {service_name}. Reason: {e}")

def create_bucket(bucket_name, project_id, credentials):
    print(f"✨ Creating Magic Bucket: {bucket_name}...")
    try:
        service = build("storage", "v1", credentials=credentials)
        bucket_body = {"name": bucket_name}
        request = service.buckets().insert(project=project_id, body=bucket_body)
        request.execute()
        print(f"✅ Bucket {bucket_name} created successfully!")
    except Exception as e:
        print(f"❌ Couldn't create bucket {bucket_name}. Reason: {e}")

def upload_model(bucket_name, model_name, credentials):
    print(f"📦 Uploading model: {model_name}...")
    try:
        service = build("storage", "v1", credentials=credentials)
        blob_name = model_name.split("/")[-1] + ".bin"
        media = {"name": blob_name}
        request = service.objects().insert(bucket=bucket_name, body=media)
        request.execute()
        print(f"✅ Model {model_name} uploaded successfully!")
    except Exception as e:
        print(f"❌ Couldn't upload model {model_name}. Reason: {e}")

def link_billing_account(project_id, billing_account_id, credentials):
    print("💳 Linking Billing Account...")
    try:
        service = build("cloudbilling", "v1", credentials=credentials)
        body = {"billingAccountName": billing_account_id}
        request = service.projects().updateBillingInfo(name=f"projects/{project_id}", body=body)
        request.execute()
        print("✅ Billing account linked successfully!")
    except Exception as e:
        print(f"❌ Couldn't link billing account. Reason: {e}")

def configure_budget(project_id, billing_account_id, credentials):
    print("📈 Configuring budget alerts...")
    try:
        service = build("cloudbilling", "v1", credentials=credentials)
        budget_body = {
            "displayName": f"Budget for {project_id}",
            "amount": {"specifiedAmount": {"currencyCode": "USD", "units": "100"}},
            "thresholdRules": [{"spendBasis": "CURRENT_SPEND", "thresholdPercent": 0.8}],
        }
        request = service.billingAccounts().budgets().create(
            parent=billing_account_id, body=budget_body
        )
        request.execute()
        print("✅ Budget alerts configured!")
    except Exception as e:
        print(f"❌ Couldn't configure budget. Reason: {e}")

def monitor_costs(project_id, billing_account_id, credentials):
    print("💰 Starting real-time cost monitoring...")
    try:
        service = build("cloudbilling", "v1", credentials=credentials)
        while True:
            response = service.billingAccounts().projects().getBillingInfo(name=f"projects/{project_id}").execute()
            current_cost = response.get("currentSpend", {}).get("amount", "N/A")
            print(f"💵 Current cost for {project_id}: ${current_cost}")
            time.sleep(60)  # Check every minute
    except Exception as e:
        print(f"❌ Couldn't monitor costs. Reason: {e}")

# Main setup flow
def main():
    credentials = authenticate_service()

    # Enable necessary APIs
    apis = ["aiplatform.googleapis.com", "bigquery.googleapis.com", "storage.googleapis.com", "compute.googleapis.com"]
    for api in apis:
        enable_api(api, PROJECT_ID, credentials)

    # Create Storage Bucket
    create_bucket(BUCKET_NAME, PROJECT_ID, credentials)

    # Upload AI Models
    for model in AI_MODELS:
        upload_model(BUCKET_NAME, model, credentials)

    # Link Billing Account
    link_billing_account(PROJECT_ID, BILLING_ACCOUNT_ID, credentials)

    # Configure Budget Alerts
    configure_budget(PROJECT_ID, BILLING_ACCOUNT_ID, credentials)

    # Start real-time cost monitoring
    monitor_costs(PROJECT_ID, BILLING_ACCOUNT_ID, credentials)

    print("🎉 All systems are ready to make magic happen!")

if __name__ == "__main__":
    main()
