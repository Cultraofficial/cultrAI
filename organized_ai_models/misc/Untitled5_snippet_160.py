# Function to upload files to Google Cloud Storage
def upload_to_gcs(local_folder, gcs_folder):
    for root, dirs, files in os.walk(local_folder):
        for file_name in files:
            local_path = os.path.join(root, file_name)
            blob = bucket.blob(f"{gcs_folder}/{file_name}")
            blob.upload_from_filename(local_path)
            print(f"Uploaded {file_name} to {gcs_folder} in GCS")

# Example: Uploading code files to the platform folder in GCS
upload_to_gcs('platform', 'platform')
upload_to_gcs('data', 'data')
upload_to_gcs('models', 'models')
upload_to_gcs('logs', 'logs')
