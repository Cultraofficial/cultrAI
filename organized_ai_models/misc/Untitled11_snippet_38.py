from google.colab import auth
from google.cloud import storage, aiplatform
from google.oauth2 import service_account
import os

# Authenticate and initialize Vertex AI
auth.authenticate_user()

# Use the correct file path for the saved credentials
project_id = "gen-lang-client-0492208227"
service_account_file = "/content/credentials.json"  # Path to the saved credentials file
credentials = service_account.Credentials.from_service_account_file(service_account_file)

# Initialize Google Cloud and Vertex AI environment
aiplatform.init(project=project_id, credentials=credentials, location="us-central1")

# Set bucket name and initialize storage client
bucket_name = "cultra_official"
storage_client = storage.Client(credentials=credentials, project=project_id)
bucket = storage_client.bucket(bucket_name)
