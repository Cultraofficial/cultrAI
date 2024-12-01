# Mount Google Drive to access files
from google.colab import drive
drive.mount('/content/drive')

# Install Google Cloud SDK and required libraries
!pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client google-cloud-storage google-cloud-aiplatform

# Authenticate with Google Cloud
from google.colab import auth
auth.authenticate_user()

# Automatic Google Cloud Variables (auto-filled)
project_id = 'gen-lang-client-0492208227'  # Based on user-provided information
bucket_name = 'cultra_official'  # Verified bucket name
config_file = 'config.yaml'
service_account_key_path = '/content/drive/My Drive/BrandNewKey.json'  # Path to your Google service account JSON key
staging_bucket = f'gs://{bucket_name}'

# Import required Google Cloud libraries
from google.cloud import storage
from google.cloud import aiplatform
from google.oauth2 import service_account

# Initialize Google Cloud Storage Client using Service Account
credentials = service_account.Credentials.from_service_account_file(service_account_key_path)
storage_client = storage.Client(project=project_id, credentials=credentials)
bucket = storage_client.bucket(bucket_name)

# Generate and Upload Configuration File
config_content = """
jobSpec:
  workerPoolSpecs:
    - machineSpec:
        machineType: n1-standard-4
      replicaCount: 1
      containerSpec:
        imageUri: "gcr.io/cloud-ml-algos/image:latest"
"""

# Write the config file locally
with open(config_file, 'w') as f:
    f.write(config_content)

# Upload config file to Google Cloud Storage
blob = bucket.blob(config_file)
blob.upload_from_filename(config_file)
print(f"Uploaded {config_file} to {bucket_name}.")

# Initialize Vertex AI API Client using Service Account and Staging Bucket
aiplatform.init(
    project=project_id,
    location="us-central1",
    credentials=credentials,
    staging_bucket=staging_bucket
)

# Set up and deploy a sample job in Vertex AI
job = aiplatform.CustomJob.from_local_script(
    display_name="vertex-ai-deployment-job",
    script_path="sample_script.py",  # Placeholder script; create or replace with actual script if needed
    container_uri="gcr.io/cloud-ml-algos/image:latest",
    machine_type="n1-standard-4",
)

# Run the job
job.run()
print("Vertex AI job deployed successfully.")
