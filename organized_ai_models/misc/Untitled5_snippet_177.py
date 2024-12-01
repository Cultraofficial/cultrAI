from google.cloud import storage

# Define Google Cloud Storage bucket name
BUCKET_NAME = 'cultra_official'

# Initialize the GCS client
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

def upload_to_gcs(local_folder, gcs_folder):
    for root, dirs, files in os.walk(local_folder):
        for file_name in files:
            local_path = os.path.join(root, file_name)
            gcs_path = os.path.join(gcs_folder, file_name)
            blob = bucket.blob(gcs_path)
            blob.upload_from_filename(local_path)
            print(f"Uploaded {local_path} to {gcs_path} in GCS")

# Example usage
upload_to_gcs('platform', 'platform')  # Upload platform files
upload_to_gcs('data', 'data')          # Upload data files
upload_to_gcs('models', 'models')      # Upload model files
