from google.cloud import storage

client = storage.Client(project="gen-lang-client-0492208227")
bucket_name = "cultra_official"
bucket = client.get_bucket(bucket_name)

# Example function to upload files to the GCS bucket
def upload_to_bucket(blob_name, file_path):
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    print(f"Uploaded {file_path} to {blob_name}")

# Use this function as needed to upload files directly
