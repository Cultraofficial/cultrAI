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

# Create a sample training script for Vertex AI to run
training_script = """
# sample_script.py content
print("Hello, Vertex AI!")
"""
with open("sample_script.py", "w") as f:
    f.write(training_script)

# Upload the training script to the bucket
blob = storage_client.bucket(bucket_name).blob("training_script.py")
blob.upload_from_filename("sample_script.py")
print("Training script uploaded to:", f"gs://{bucket_name}/training_script.py")

# Run a Vertex AI Custom Job with minimal resource settings
job = aiplatform.CustomJob.from_local_script(
    display_name="vertex-ai-test-job",
    script_path="sample_script.py",
    container_uri="gcr.io/deeplearning-platform-release/tf2-cpu.2-6:latest",  # Public TensorFlow image
    requirements=["google-cloud-aiplatform", "google-cloud-storage"],
    replica_count=1,
    machine_type="n1-standard-2",  # Lower resource machine
)

# Submit the job to Vertex AI
job.run(sync=False)  # Setting sync=False to allow asynchronous execution
print("Custom job submitted.")
