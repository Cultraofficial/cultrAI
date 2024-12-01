from google.cloud import storage

# Initialize Google Cloud Storage client
project_id = "gen-lang-client-0492208227"
bucket_name = "cultra_official"
storage_client = storage.Client(project=project_id)
bucket = storage_client.bucket(bucket_name)

def list_all_files_in_bucket():
    print(f"Listing all contents in 'gs://{bucket_name}'...\n")
    blobs = list(bucket.list_blobs())

    if blobs:
        print("Files and directories found in the bucket:")
        for blob in blobs:
            print(f" - {blob.name} (Size: {blob.size} bytes)")
    else:
        print(f"No files or directories found in 'gs://{bucket_name}'.")

# Run the check
list_all_files_in_bucket()
