import os
from google.cloud import storage

# Initialize Google Cloud Storage client with the service account
storage_client = storage.Client.from_service_account_json('/content/drive/My Drive/BrandNewKey.json')

# Define the bucket and folder path
bucket_name = 'cultra_official'
folder_path = 'platform/'

# Define local directory for Vertex
local_directory = '/vertex_ai_workspace/'

# Create the directory if it does not exist
os.makedirs(local_directory, exist_ok=True)

# Connect to the bucket
bucket = storage_client.get_bucket(bucket_name)

# Download files from the bucket to Vertex AI environment
for blob in bucket.list_blobs(prefix=folder_path):
    local_path = os.path.join(local_directory, blob.name.split('/')[-1])
    blob.download_to_filename(local_path)
    print(f"Downloaded {blob.name} to {local_path}")
