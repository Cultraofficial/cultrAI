# Import necessary libraries
from google.cloud import aiplatform
from google.oauth2 import service_account
from google.cloud import storage

# Define service account details and bucket information (apply values automatically as per authorization)
service_account_key_path = '/content/drive/My Drive/BrandNewKey.json'
project_id = 'gen-lang-client-0492208227'
bucket_name = 'cultra_official'
staging_bucket = f'gs://{bucket_name}'

# Initialize credentials
credentials = service_account.Credentials.from_service_account_file(service_account_key_path)

# Initialize Vertex AI API Client using Service Account and Staging Bucket
aiplatform.init(
    project=project_id,
    location="us-central1",
    credentials=credentials,
    staging_bucket=staging_bucket
)

# Create and upload a simple Python training script to Google Cloud Storage
python_script = """
import time

if __name__ == "__main__":
    for i in range(10):
        print(f"Step {i+1}/10: Training in progress...")
        time.sleep(1)
    print("Training complete!")
"""

# Save the script to a file
script_path = "training_script.py"
with open(script_path, "w") as f:
    f.write(python_script)

# Upload the script to Google Cloud Storage
gcs_uri = f"{staging_bucket}/training_script.py"
storage_client = storage.Client(credentials=credentials)
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob("training_script.py")
blob.upload_from_filename(script_path)
print("Training script uploaded to:", gcs_uri)

# Define and submit a CustomJob to Vertex AI
job = aiplatform.CustomJob(
    display_name="alternative-deployment-job",
    worker_pool_specs=[
        {
            "machine_spec": {
                "machine_type": "n1-standard-4",
            },
            "replica_count": 1,
            "python_package_spec": {
                "executor_image_uri": "us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-6:latest",  # Use a TensorFlow CPU image
                "package_uris": [gcs_uri],
                "python_module": "training_script",  # Name without `.py` extension
            },
        }
    ],
)

# Run the job
job.run()
print("Vertex AI job deployed successfully.")
