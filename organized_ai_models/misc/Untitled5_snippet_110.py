# Install necessary libraries if not already installed
!pip install google-cloud-storage google-cloud-firestore google-cloud-aiplatform

# Authenticate with Google Cloud
from google.colab import auth
auth.authenticate_user()

# Project and region configuration
PROJECT_ID = "cultra-2ffad"  # Use your actual project ID
REGION = "us-central1"       # Set your preferred region

# Ensure environment variables are set
import os
os.environ["GOOGLE_CLOUD_PROJECT"] = PROJECT_ID
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY_PATH

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
