# Set up Google Cloud Storage bucket
BUCKET_NAME = "cultra_official"  # Replace with your actual bucket name
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

# Test bucket access by listing files
blobs = list(bucket.list_blobs(prefix="platform/"))
print("Files in the 'platform' directory:")
for blob in blobs:
    print(blob.name)
