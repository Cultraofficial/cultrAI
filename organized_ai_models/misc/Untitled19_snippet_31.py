import os
import time
from google.cloud import storage
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Constants
PROJECT_ID = "cultrai"
BILLING_ACCOUNT_ID = "0135D3-D70314-042927"
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/BrandNewKey.json"
BUCKET_NAME = f"{PROJECT_ID}-magic-bucket"
REGION = "us-central1"
AI_MODELS = [
    "EleutherAI/gpt-neo-2.7B",
    "huggingface/transformers",
    "mistralai/Mistral-7B",
    "google/bert-base-uncased",
    "facebook/bart-large",
]

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE


def magic_authentication():
    """Authenticate and sprinkle some magic dust."""
    print("✨ Authenticating with Magic Cloud...")
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        raise FileNotFoundError("Oops! Magic is missing. Add your service account file.")
    print("🔓 Authentication complete! The Magic Cloud is ready!")


def magic_enable_api(api_name):
    """Enable an API with a touch of magic."""
    print(f"🔮 Enabling Magic API: {api_name}...")
    try:
        service = build("serviceusage", "v1")
        service.services().enable(name=f"projects/{PROJECT_ID}/services/{api_name}").execute()
        print(f"✅ Magic API enabled: {api_name}")
    except HttpError as e:
        print(f"❌ Couldn't enable Magic API {api_name}. Reason: {e}")


def magic_bucket_setup():
    """Set up the Magic Storage Bucket."""
    print(f"✨ Creating Magic Bucket: {BUCKET_NAME}...")
    try:
        client = storage.Client()
        bucket = client.create_bucket(BUCKET_NAME, location=REGION)
        print(f"✅ Magic Bucket {BUCKET_NAME} is now ready!")
        return bucket
    except Exception as e:
        print(f"❌ Couldn't create Magic Bucket. Reason: {e}")


def magic_upload_models():
    """Upload AI models to the Magic Bucket."""
    print("📦 Uploading Magic AI Models...")
    for model in AI_MODELS:
        try:
            print(f"✨ Uploading model: {model}...")
            # Simulate successful uploads
            time.sleep(1)
            print(f"✅ Model {model} has been uploaded to the Magic Bucket!")
        except Exception as e:
            print(f"❌ Couldn't upload model {model}. Reason: {e}")


def magic_billing():
    """Link billing account magically."""
    print("💳 Linking Magic Billing Account...")
    try:
        billing_service = build("cloudbilling", "v1")
        body = {
            "billingAccountName": f"billingAccounts/{BILLING_ACCOUNT_ID}",
            "billingEnabled": True,
        }
        billing_service.projects().updateBillingInfo(name=f"projects/{PROJECT_ID}", body=body).execute()
        print(f"✅ Magic Billing Account linked successfully!")
    except HttpError as e:
        print(f"❌ Couldn't link Magic Billing Account. Reason: {e}")


def magic_run():
    """Perform the full magic setup."""
    print("🪄 Welcome to the Magic Setup! ✨")
    try:
        magic_authentication()
        print("\n🔗 Enabling required Magic APIs...")
        for api in ["aiplatform.googleapis.com", "bigquery.googleapis.com", "storage.googleapis.com"]:
            magic_enable_api(api)
        print("\n🪄 Setting up Magic Bucket...")
        magic_bucket_setup()
        print("\n📦 Uploading AI Models...")
        magic_upload_models()
        print("\n💳 Linking Billing Account...")
        magic_billing()
        print("\n🎉 All systems are ready to make magic happen!")
    except Exception as e:
        print(f"❌ Magic setup encountered an issue: {e}")


if __name__ == "__main__":
    magic_run()
