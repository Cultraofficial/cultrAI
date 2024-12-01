import os
from google.cloud import storage

# Initialize the Google Cloud Storage client
client = storage.Client()
bucket = client.bucket('cultra_official')  # Replace with your GCS bucket name

def upload_to_gcs(local_folder, gcs_folder):
    for root, dirs, files in os.walk(local_folder):
        for file_name in files:
            local_path = os.path.join(root, file_name)
            blob_path = os.path.join(gcs_folder, file_name)
            blob = bucket.blob(blob_path)
            blob.upload_from_filename(local_path)
            print(f"Uploaded {local_path} to gs://{bucket.name}/{blob_path}")

# Example usage
# Replace 'platform', 'data', 'models' with the paths to your local folders
upload_to_gcs('/content/platform', 'platform')
upload_to_gcs('/content/data', 'data')
upload_to_gcs('/content/models', 'models')
