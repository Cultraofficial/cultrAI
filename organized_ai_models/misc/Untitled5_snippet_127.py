# Import required libraries
from google.cloud import storage, firestore, aiplatform
import google.auth
import time

# Mount Google Drive to access stored credentials
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# Define path to the JSON service account key based on prior setup
json_key_path = "/content/drive/My Drive/BrandNewKey.json"  # Correct JSON key path

# Authenticate using the JSON service account key
!gcloud auth activate-service-account --key-file="{json_key_path}"

# Define the correct project ID automatically retrieved from past information
project_id = "cultra_project_id"  # This should be your actual project ID as found from past conversations

# Initialize Firestore Client with the correct project ID and credentials
credentials, _ = google.auth.default()
db = firestore.Client(project=project_id, credentials=credentials)

# Initialize Google Cloud Storage Client
storage_client = storage.Client(credentials=credentials, project=project_id)

# Initialize Vertex AI Platform with the correct project ID and location
aiplatform.init(project=project_id, location="us-central1")

# Step 2: Verify Google Cloud Storage Access
def list_bucket_contents(bucket_name, folder_prefix):
    """List contents in the specified Google Cloud Storage bucket folder."""
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_prefix)
    for blob in blobs:
        print(blob.name)

# List contents of the 'cultra_official' bucket in the 'platform' folder
list_bucket_contents('cultra_official', 'platform')

# Step 3: Verify Firestore Connection by adding a sample entry
def verify_firestore_connection():
    """Add a test entry to Firestore to verify connection."""
    test_ref = db.collection('system_checks').document('firestore_test')
    test_ref.set({
        'status': 'connected',
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    print("Firestore connection verified and test entry added.")

verify_firestore_connection()

# Additional functionalities follow as previously described
# ...
