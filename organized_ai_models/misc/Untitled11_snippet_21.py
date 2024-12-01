import os
from google.colab import drive
from google.cloud import storage
from google.cloud import aiplatform

# Mount Google Drive
drive.mount('/content/drive')

# Set up Google Cloud Project ID and other credentials
project_id = "gen-lang-client-0492208227"
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"  # Replace with the path to your JSON key file if different

# Authenticate Google Cloud
!gcloud auth activate-service-account --key-file="$GOOGLE_APPLICATION_CREDENTIALS"
!gcloud config set project $GOOGLE_CLOUD_PROJECT

# Clone the GitHub repository
repo_url = "https://github.com/Cultraofficial/sacrifice-in-Cultra.git"
!git clone $repo_url
os.chdir("sacrifice-in-Cultra")

# Configure Git credentials
!git config --global user.email "tropicalstormllc@gmail.com"  # Replace with your GitHub email
!git config --global user.name "Cultraofficial"

# Create the .github/workflows/deploy-to-vertex-ai.yml file
workflow_content = """
name: Deploy to Vertex AI

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Google Cloud SDK
        uses: google-github-actions/setup-gcloud@master
        with:
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          service_account_key: '${{ secrets.GOOGLE_APPLICATION_CREDENTIALS }}'

      - name: Deploy Model
        run: |
          gcloud ai custom-jobs create \
            --region=us-central1 \
            --display-name="vertex-ai-deployment-job" \
            --python-package-uris="gs://cultragroundzero/training_script.py" \
            --python-module="main_script" \
            --args="--training_steps=1000,--learning_rate=0.001"
"""

# Save the workflow content to a new file
os.makedirs(".github/workflows", exist_ok=True)
with open(".github/workflows/deploy-to-vertex-ai.yml", "w") as f:
    f.write(workflow_content)

# Commit and push the changes to GitHub
!git add .
!git commit -m "Add workflow and training script"
!git push origin main
