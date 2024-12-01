# Required imports
import os
from google.colab import drive
from google.cloud import aiplatform, storage
from google.oauth2 import service_account

# Mount Google Drive (where service account key is stored)
drive.mount('/content/drive')

# Automatically set project details from prior context
project_id = "gen-lang-client-0492208227"  # Use the exact project ID you shared
bucket_name = "cultragroundzero"  # Updated bucket name
script_path = "gs://cultragroundzero/REPO_URL_1/main.py"  # Adjust to the actual path in your bucket
service_account_key_path = "/content/drive/My Drive/BrandNewKey.json"  # Update path to where your JSON key is stored

# Authenticate and initialize clients
credentials = service_account.Credentials.from_service_account_file(service_account_key_path)
aiplatform.init(project=project_id, location="us-central1", staging_bucket=bucket_name, credentials=credentials)
storage_client = storage.Client(project=project_id, credentials=credentials)

# Clone repositories (Replace REPO_URLs with actual URLs)
os.system("git clone REPO_URL_1 /content/repo1")  # Example: Replace REPO_URL_1 with the actual URL
os.system("git clone REPO_URL_2 /content/repo2")  # Example: Replace REPO_URL_2 with the actual URL
print("Repositories cloned successfully.")

# Upload the training script to GCS
blob = storage_client.bucket(bucket_name).blob("training_script.py")
blob.upload_from_filename("/content/repo1/main.py")  # Adjust this if the main script is in a different location
print(f"Training script uploaded to: gs://{bucket_name}/training_script.py")

# Submit a Vertex AI Custom Job using the uploaded script
job = aiplatform.CustomJob.from_local_script(
    display_name="vertex-ai-deployment-job",
    script_path=script_path,
    container_uri="gcr.io/deeplearning-platform-release/tf2-cpu.2-3:latest",
    project=project_id,
    location="us-central1",
    staging_bucket=bucket_name,
    credentials=credentials
)

# Run the job asynchronously
job.run(sync=False)
print("Custom job submitted. Check status in the Google Cloud Console.")

# Print link for easy access
print(f"Monitor job at: https://console.cloud.google.com/ai/platform/locations/us-central1/training/{job.resource_name}?project={project_id}")
