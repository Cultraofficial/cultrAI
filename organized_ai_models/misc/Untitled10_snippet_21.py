from google.colab import drive
from google.cloud import storage, aiplatform
import os

# Mount Google Drive
drive.mount('/content/drive', force_remount=True)

# Automatically applied Google Cloud project ID and service account JSON path
project_id = 'gen-lang-client-0492208227'  # Replace with project ID if incorrect
service_account_json = '/content/drive/My Drive/BrandNewKey.json'  # Use this JSON path as specified

# Authenticate with Google Cloud
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_json
aiplatform.init(project=project_id, location="us-central1")

print("Authenticated with Google Cloud.")
