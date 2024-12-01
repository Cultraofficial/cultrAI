import os
from google.cloud import storage

# Set the Google Application Credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"

# Initialize Google Cloud Storage client with the project ID
client = storage.Client(project="gen-lang-client-0492208227")
bucket_name = "cultra_official"
bucket = client.get_bucket(bucket_name)

# Example function to upload files to the GCS bucket
def upload_to_bucket(blob_name, file_path):
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    print(f"Uploaded {file_path} to {blob_name}")

# Test the upload function if you have a file to upload
# upload_to_bucket("your_blob_name", "path_to_your_local_file")
