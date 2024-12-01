# Assuming credentials and project setup are already done in Colab
from google.cloud import aiplatform, storage

# Initialize Vertex AI
aiplatform.init(project='gen-lang-client-0492208227', location='us-central1')

# Test access to Cloud Storage
storage_client = storage.Client()
bucket_name = 'cultragroundzero'
bucket = storage_client.bucket(bucket_name)
blobs = bucket.list_blobs()
print("Files in bucket:")
for blob in blobs:
    print(blob.name)

# List available models in Vertex AI
models = aiplatform.Model.list()
print("Available models in Vertex AI:")
for model in models:
    print(f"- {model.display_name} (ID: {model.resource_name})")
