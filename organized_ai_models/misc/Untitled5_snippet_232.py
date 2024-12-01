from google.cloud import storage
from google.cloud import aiplatform
from huggingface_hub import login

# Authenticate with Hugging Face
huggingface_token = "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"  # Replace with your latest token if necessary
login(huggingface_token)

# Google Cloud Project and Bucket information
project_id = "gen-lang-client-0492208227"
bucket_name = "cultra_official"
region = "us-central1"

# Initialize Vertex AI and Storage Client
aiplatform.init(project=project_id, location=region)
storage_client = storage.Client(project=project_id)
bucket = storage_client.get_bucket(bucket_name)
