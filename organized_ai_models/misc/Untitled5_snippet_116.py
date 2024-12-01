import google.cloud.storage as storage

# Initialize the client
client = storage.Client()

# Specify the bucket name
bucket = client.get_bucket('cultra_official')

# Check access to the 'platform' folder
folder = 'platform'
blobs = bucket.list_blobs(prefix=folder)
for blob in blobs:
    print(blob.name)
