from google.oauth2 import service_account
from google.cloud import bigquery
from google.cloud import aiplatform
import os

# Path to your service account key file
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/BrandNewKey.json"
PROJECT_ID = "gen-lang-client-0492208227"

# Authenticate using service account
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)

# Verify authentication
try:
    client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
    print("BigQuery authentication successful!")
    aiplatform.init(project=PROJECT_ID, credentials=credentials)
    print("Vertex AI authentication successful!")
except Exception as e:
    print(f"Authentication failed: {e}")
