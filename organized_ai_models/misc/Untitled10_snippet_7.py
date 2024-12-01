# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Install required packages
!pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client google-cloud-storage google-cloud-aiplatform

import os
from google.cloud import storage, aiplatform
from google.oauth2 import service_account

# Configuration details
project_id = "gen-lang-client-0492208227"
region = "us-central1"
bucket_name = "cultragroundzero"
service_account_key_path = "/content/drive/My Drive/BrandNewKey.json"  # Ensure this path is accurate

# Initialize Google Cloud with Service Account
credentials = service_account.Credentials.from_service_account_file(service_account_key_path)

# Initialize the Storage Client
storage_client = storage.Client(project=project_id, credentials=credentials)
bucket = storage_client.bucket(bucket_name)

# Initialize Vertex AI with Service Account and specify the staging bucket
aiplatform.init(
    project=project_id,
    location=region,
    staging_bucket=f"gs://{bucket_name}",
    credentials=credentials
)

# Upload a sample training script to Google Cloud Storage
training_script_path = "training_script.py"
with open(training_script_path, "w") as f:
    f.write("""
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=5)
    args = parser.parse_args()
    for epoch in range(args.epochs):
        print(f"Epoch {epoch+1} completed.")
if __name__ == '__main__':
    main()
""")

# Upload training script to Cloud Storage
training_script_blob = bucket.blob("training_script.py")
training_script_blob.upload_from_filename(training_script_path)
print(f"Training script uploaded to: gs://{bucket_name}/training_script.py")

# Create and submit a Vertex AI Custom Job
try:
    job = aiplatform.CustomJob.from_local_script(
        display_name="vertex-ai-deployment-job",
        script_path=training_script_path,
        container_uri="gcr.io/cloud-ml-algos/image:latest",  # Adjust if you have a specific container image
        args=["--epochs", "10"],
        replica_count=1,
        machine_type="n1-standard-4",
        staging_bucket=f"gs://{bucket_name}"
    )
    job.run(sync=True)
    print("Job completed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
