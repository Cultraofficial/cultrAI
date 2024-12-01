from google.colab import drive
from google.cloud import aiplatform, storage
from google.oauth2 import service_account

# Mount Google Drive to access the service account key
drive.mount('/content/drive')

# Path to service account key file in Google Drive
service_account_key_path = '/content/drive/My Drive/BrandNewKey.json'

# Initialize credentials and project details
project_id = 'gen-lang-client-0492208227'
bucket_name = 'cultragroundzero'  # Use the new bucket name
region = 'us-central1'  # Ensure this matches the bucket's region

# Load service account credentials
credentials = service_account.Credentials.from_service_account_file(service_account_key_path)

# Initialize Vertex AI with the specified project and region
aiplatform.init(project=project_id, location=region, credentials=credentials, staging_bucket=f"gs://{bucket_name}")

# Initialize Google Cloud Storage Client
storage_client = storage.Client(project=project_id, credentials=credentials)
bucket = storage_client.bucket(bucket_name)

# Upload configuration or any additional files to the new bucket
config_content = """
# Sample configuration content for Vertex AI job
training_config:
  parameter: value
"""
config_blob = bucket.blob("config.yaml")
config_blob.upload_from_string(config_content)

# Sample training script to be uploaded to the bucket
with open("training_script.py", "w") as script_file:
    script_file.write("""
# Sample training script
print("Training job executed successfully.")
""")
training_script_blob = bucket.blob("training_script.py")
training_script_blob.upload_from_filename("training_script.py")

# Create a custom job in Vertex AI using the new bucket
job = aiplatform.CustomJob.from_local_script(
    display_name="vertex-ai-deployment-job",
    script_path="training_script.py",
    container_uri="gcr.io/cloud-ml-algos/image:latest",
    staging_bucket=f"gs://{bucket_name}",
    project=project_id,
    location=region,
    credentials=credentials,
)

# Run the custom job
job.run(sync=True)
