import os
from google.cloud import storage

# Initialize Google Cloud storage client
storage_client = storage.Client.from_service_account_json(service_account_path)

# Define the bucket and folder path
bucket_name = 'cultra_official'  # Adjust if the bucket name is different
folder_path = 'platform/'  # Adjust if the folder structure is different

# Connect to the bucket
bucket = storage_client.get_bucket(bucket_name)

# List and process files in the specified folder
blobs = bucket.list_blobs(prefix=folder_path)
for blob in blobs:
    print(f"Processing file: {blob.name}")
    # Here, you can add the code to process each file as required by your AI model
