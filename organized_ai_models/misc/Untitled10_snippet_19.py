# Step 1: Mount Google Drive to access the service account key
from google.colab import drive
drive.mount('/content/drive')

# Step 2: Install necessary Google Cloud libraries
!pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client google-cloud-storage google-cloud-aiplatform

# Step 3: Import required libraries
import os
from google.cloud import storage
from google.cloud import aiplatform
from google.auth import credentials
from google.auth.transport.requests import Request

# Step 4: Set up Google Cloud Project, Service Account, and Storage Bucket
project_id = "gen-lang-client-0492208227"  # Project ID based on your information
region = "us-central1"  # Vertex AI region
bucket_name = "cultragroundzero"  # Your bucket name
service_account_key_path = "/content/drive/My Drive/BrandNewKey.json"  # Path to your service account key

# Step 5: Authenticate with Google Cloud
print("Authenticating with Google Cloud...")
!gcloud auth activate-service-account --key-file="{service_account_key_path}" > /dev/null 2>&1
!gcloud config set project {project_id} > /dev/null 2>&1

# Initialize Vertex AI with the project and location
aiplatform.init(project=project_id, location=region)

# Step 6: Clone GitHub Repository Automatically
repo_url = "https://github.com/Cultraofficial/sacrifice-in-Cultra.git"  # Repository URL based on previous context
repo_dir = "/content/sacrifice-in-Cultra"

# Check if the repository already exists, otherwise clone it
if not os.path.exists(repo_dir):
    print("Cloning repository...")
    !git clone {repo_url} {repo_dir}
else:
    print("Repository already exists.")

# Step 7: Locate the Main Training Script in the Repository
# Assumes main script is named "main_script.py"; adjust if necessary
training_script_path = os.path.join(repo_dir, "main_script.py")
if not os.path.exists(training_script_path):
    raise FileNotFoundError("Training script (main_script.py) not found in the cloned repository.")

# Step 8: Upload Training Script to Google Cloud Storage
print("Uploading training script to Google Cloud Storage...")
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob("training_script.py")
blob.upload_from_filename(training_script_path)
print("Training script uploaded to:", f"gs://{bucket_name}/training_script.py")

# Step 9: Submit Custom Job to Vertex AI
print("Submitting custom job to Vertex AI...")
custom_job = aiplatform.CustomJob.from_local_script(
    display_name="vertex-ai-deployment-job",
    script_path=training_script_path,
    container_uri="gcr.io/cloud-ml-algos/image:latest",  # Default container, update if needed
    args=["--training_steps=1000", "--learning_rate=0.001"],  # Customize arguments as needed
    project=project_id,
    staging_bucket=f"gs://{bucket_name}",
    location=region
)

# Run the job
custom_job.run()
print("Custom job submitted successfully. Check Vertex AI for status updates.")

# Step 10: Verify Setup (Check for Output or Errors)
print("Setup complete. Monitor Vertex AI dashboard for job progress.")
