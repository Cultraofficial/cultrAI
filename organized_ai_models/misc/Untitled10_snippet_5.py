from google.cloud import aiplatform
from google.oauth2 import service_account
from google.cloud import storage

# Set up service account credentials
service_account_key_path = '/content/drive/My Drive/BrandNewKey.json'
project_id = "gen-lang-client-0492208227"
staging_bucket = "gs://cultra_bucket"  # Your bucket in us-central1

# Initialize Google Cloud credentials
credentials = service_account.Credentials.from_service_account_file(service_account_key_path)

# Initialize Vertex AI with the new bucket and us-central1 location
aiplatform.init(
    project=project_id,
    location="us-central1",
    staging_bucket=staging_bucket,
    credentials=credentials
)

# Sample job configuration for deploying to Vertex AI
job = aiplatform.CustomJob.from_local_script(
    display_name="vertex-ai-deployment-job",
    script_path="training_script.py",  # Replace with your script if different
    container_uri="us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-8:latest",  # Example container, replace if needed
    staging_bucket=staging_bucket,
)

# Submit the job
job.run(sync=True)
