# Import necessary libraries
from google.colab import drive
from google.oauth2 import service_account
from google.cloud import aiplatform
from google.cloud import storage

# Mount Google Drive to access service account key
drive.mount('/content/drive')

# Set up the path to the service account key file
service_account_key_path = '/content/drive/My Drive/BrandNewKey.json'

# Initialize Google Cloud credentials
credentials = service_account.Credentials.from_service_account_file(service_account_key_path)
project_id = "gen-lang-client-0492208227"
bucket_name = "cultragroundzero"
location = "us-central1"  # Ensure this matches the region of your resources

# Initialize the Vertex AI API client
aiplatform.init(
    project=project_id,
    location=location,
    staging_bucket=f"gs://{bucket_name}",
    credentials=credentials,
)

# Initialize Google Cloud Storage Client
storage_client = storage.Client(project=project_id, credentials=credentials)
bucket = storage_client.bucket(bucket_name)

# Create a configuration file (if required for the job)
config_content = """
# Sample configuration content
"""
config_blob = bucket.blob("config.yaml")
config_blob.upload_from_string(config_content)
print("Uploaded config.yaml to", bucket_name)

# Create a sample training script for Vertex AI to run
training_script = """
# sample_script.py content
print("Hello, Vertex AI!")
"""
with open("sample_script.py", "w") as f:
    f.write(training_script)

# Upload the training script to the bucket
blob = bucket.blob("training_script.py")
blob.upload_from_filename("sample_script.py")
print("Training script uploaded to:", f"gs://{bucket_name}/training_script.py")

# Run a Vertex AI Custom Job
job = aiplatform.CustomJob.from_local_script(
    display_name="vertex-ai-deployment-job",
    script_path="sample_script.py",
    container_uri="gcr.io/cloud-ml-algos/image:latest",  # This URI may require the Vertex AI service account to have access
    requirements=["google-cloud-aiplatform", "google-cloud-storage"],
    replica_count=1,
    machine_type="n1-standard-4",
)

# Submit the job to Vertex AI
job.run(sync=True)
print("Custom job completed successfully.")
