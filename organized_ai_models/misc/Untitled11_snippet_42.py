from google.cloud import aiplatform, storage
import os

# Initialize Vertex AI SDK and Google Cloud Storage
project_id = "gen-lang-client-0492208227"
location = "us-central1"
bucket_name = "cultra_official"

aiplatform.init(project=project_id, location=location)
storage_client = storage.Client(project=project_id)
bucket = storage_client.bucket(bucket_name)
