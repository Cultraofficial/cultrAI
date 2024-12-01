from google.cloud import storage
import os

# Ensure Google Cloud credentials are set up
service_account_path = '/content/drive/My Drive/BrandNewKey.json'
storage_client = storage.Client.from_service_account_json(service_account_path)

# Define the bucket and folder path for saving processed files
bucket_name = 'cultra_official'
folder_path = 'platform/processed/'  # Adjust as needed

# Connect to the bucket
bucket = storage_client.get_bucket(bucket_name)

# Upload processed files from Colab to Google Cloud Storage
local_directory = '/vertex_ai_workspace/'  # Use the same directory if files are saved here
for filename in os.listdir(local_directory):
    local_path = os.path.join(local_directory, filename)
    remote_path = folder_path + filename

    # Upload file
    blob = bucket.blob(remote_path)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {filename} to {remote_path}")
