# Import necessary libraries
from google.cloud import storage, firestore, aiplatform
import google.auth

# Mount Google Drive to access JSON key file if needed
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# Set up the JSON key path for the chosen project (Gemini API)
json_key_path = "/content/drive/My Drive/BrandNewKey.json"  # Adjust to the exact JSON file path if needed

# Authenticate using the JSON key file
!gcloud auth activate-service-account --key-file="{json_key_path}"

# Set the selected project ID
project_id = "gen-lang-client-0492208227"

# Initialize Firestore and Storage Clients with global scope
credentials, _ = google.auth.default()
db = firestore.Client(project=project_id, credentials=credentials)
storage_client = storage.Client(credentials=credentials, project=project_id)

# Initialize Vertex AI with the correct project ID and location
aiplatform.init(project=project_id, location="us-central1")
print("Google Cloud services initialized successfully.")

# Verify Firestore connection
def verify_firestore_connection():
    try:
        test_ref = db.collection('system_checks').document('firestore_test')
        test_ref.set({
            'status': 'connected',
            'timestamp': firestore.SERVER_TIMESTAMP
        })
        print("Firestore connection verified.")
    except Exception as e:
        print("Firestore verification failed:", e)

verify_firestore_connection()

# List contents of a specific bucket folder to verify Storage access
def list_bucket_contents(bucket_name, folder_prefix):
    """List contents in the specified Google Cloud Storage bucket folder."""
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=folder_prefix)
        for blob in blobs:
            print(blob.name)
        print("Google Cloud Storage access verified.")
    except Exception as e:
        print("Storage verification failed:", e)

# Replace 'cultra_official' with your actual bucket name and 'platform' with folder prefix
list_bucket_contents('cultra_official', 'platform')
