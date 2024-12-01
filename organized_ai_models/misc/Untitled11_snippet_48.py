from google.cloud import aiplatform
from google.oauth2 import service_account

# Specify the path to your service account key file
service_account_file = "/content/credentials.json"  # Path to the saved JSON key file

# Load credentials from the JSON key file
credentials = service_account.Credentials.from_service_account_file(service_account_file)

# Initialize Vertex AI with credentials
project_id = "gen-lang-client-0492208227"
location = "us-central1"
aiplatform.init(project=project_id, location=location, credentials=credentials)
