from google.oauth2 import service_account
from google.cloud import aiplatform, storage

# Path to your JSON key file in Google Drive
service_account_path = "/content/drive/My Drive/BrandNewKey.json"  # Adjust if needed
project_id = "gen-lang-client-0492208227"  # Replace with your project ID

# Authenticate and initialize Google Cloud clients
credentials = service_account.Credentials.from_service_account_file(service_account_path)
aiplatform.init(project=project_id, location="us-central1", credentials=credentials)
storage_client = storage.Client(credentials=credentials, project=project_id)
