from google.cloud import aiplatform
from google.oauth2 import service_account
from google.cloud import storage

# Set project details and credentials
project_id = "gen-lang-client-0492208227"
location = "us-central1"
bucket_name = "cultra_official"
model_folder = "models"  # Folder in the bucket containing model files
service_account_path = "/content/drive/My Drive/gitkey.json"  # Ensure this path is correct

# Authenticate using the service account JSON key
credentials = service_account.Credentials.from_service_account_file(service_account_path)

# Initialize Vertex AI with credentials
aiplatform.init(project=project_id, location=location, credentials=credentials)

# Verify access to the bucket and list model files
storage_client = storage.Client(credentials=credentials, project=project_id)
bucket = storage_client.bucket(bucket_name)
blobs = bucket.list_blobs(prefix=model_folder)

print("Files in 'cultra_official/models' bucket folder:")
for blob in blobs:
    print(blob.name)

# Set model deployment parameters
model_file = "aiplatform_custom_trainer_script-0.1.tar.gz"  # Update with actual model name if needed
model_path = f"gs://{bucket_name}/{model_folder}/{model_file}"

# Deploy model to Vertex AI
try:
    model = aiplatform.Model.upload(
        display_name="my_model",
        artifact_uri=model_path,
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-3:latest",
        credentials=credentials
    )
    model.wait()
    print(f"Model deployed with ID: {model.resource_name}")
except Exception as e:
    print("Failed to deploy the model:", e)
