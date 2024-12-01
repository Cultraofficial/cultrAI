# Mount Google Drive to access the service account key file
from google.colab import drive
drive.mount('/content/drive')

# Define your project ID and region
PROJECT_ID = "cultra-2ffad"  # Replace with your actual project ID
REGION = "us-central1"       # Set your preferred region

# Path to your service account key file
SERVICE_ACCOUNT_KEY_PATH = "/content/drive/My Drive/service-account-key.yaml"  # Update if necessary

# Set environment variables for authentication
import os
os.environ["GOOGLE_CLOUD_PROJECT"] = PROJECT_ID
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY_PATH

# Activate the service account using the key file
!gcloud auth activate-service-account --key-file="$SERVICE_ACCOUNT_KEY_PATH"

# Initialize Vertex AI
from google.cloud import aiplatform
aiplatform.init(project=PROJECT_ID, location=REGION)
print("Vertex AI initialized successfully.")

# Set up Google Cloud Storage
from google.cloud import storage
storage_client = storage.Client()
BUCKET_NAME = "cultra_official"  # Use your bucket name here
bucket = storage_client.bucket(BUCKET_NAME)

# Test bucket access by listing files in the 'platform' folder
blobs = list(bucket.list_blobs(prefix="platform/"))
print("Files in the 'platform' directory:")
for blob in blobs:
    print(blob.name)

# Initialize Firestore client
from google.cloud import firestore
firestore_client = firestore.Client()
print("Firestore initialized successfully.")

# Confirmation of successful setup
print("Setup complete: Google Cloud Storage, Firestore, and Vertex AI are ready.")
