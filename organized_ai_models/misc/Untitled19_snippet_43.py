from google.cloud import storage

# Initialize a storage client to verify authentication
client = storage.Client()
buckets = list(client.list_buckets())
print(f"Connected! Available buckets: {[bucket.name for bucket in buckets]}")
