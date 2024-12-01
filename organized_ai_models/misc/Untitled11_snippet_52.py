from google.cloud import storage

# Initialize Cloud Storage client
storage_client = storage.Client(project=project_id)
bucket = storage_client.bucket("cultra_official")

# Specify the local path to T5-XXL model files
local_model_path = "/path/to/your/local/t5_xxl_model_files"

# Define the destination path in Cloud Storage
destination_folder = "models/t5_xxl"

# Upload each file in the model directory to Cloud Storage
import os

for root, _, files in os.walk(local_model_path):
    for file in files:
        local_file_path = os.path.join(root, file)
        destination_blob_path = os.path.join(destination_folder, os.path.relpath(local_file_path, local_model_path))
        blob = bucket.blob(destination_blob_path)
        blob.upload_from_filename(local_file_path)
        print(f"Uploaded {local_file_path} to gs://{bucket.name}/{destination_blob_path}")
