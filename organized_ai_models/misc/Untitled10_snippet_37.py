import os
from google.oauth2 import service_account
from google.cloud import aiplatform, storage

# Automatically applied paths based on past conversations
service_account_path = "/content/drive/My Drive/BrandNewKey.json"  # Path to your JSON key file

credentials = service_account.Credentials.from_service_account_file(service_account_path)
project_id = "gen-lang-client-0492208227"  # Automatically applied project ID

# Initialize AI Platform
aiplatform.init(project=project_id, location="us-central1", credentials=credentials)
storage_client = storage.Client(credentials=credentials, project=project_id)
