# Import necessary libraries
from google.cloud import storage, firestore, aiplatform
import google.auth

# Mount Google Drive to access JSON key file if needed
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# Set up the JSON key path for the chosen project
json_key_path = "/content/drive/My Drive/BrandNewKey.json"  # Update if needed

# Authenticate using the JSON key file
!gcloud auth activate-service-account --key-file="{json_key_path}"

# Define the selected project ID
project_id = "gen-lang-client-0492208227"

# Initialize Firestore and Storage Clients with global scope
credentials, _ = google.auth.default()
db = firestore.Client(project=project_id, credentials=credentials)
storage_client = storage.Client(credentials=credentials, project=project_id)

# Initialize Vertex AI with the correct project ID and location (for future use)
aiplatform.init(project=project_id, location="us-central1")
print("Google Cloud services initialized successfully.")
