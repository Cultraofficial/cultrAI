# Create the .github/workflows directory if it doesn't exist
!mkdir -p /content/sacrifice-in-Cultra/.github/workflows

# Write a sample GitHub Actions workflow file for deploying to Vertex AI
with open("/content/sacrifice-in-Cultra/.github/workflows/deploy-to-vertex-ai.yml", "w") as file:
    file.write("""
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
          version: 'latest'
          service_account_key: ${{ secrets.GOOGLE_APPLICATION_CREDENTIALS }}
          project_id: 'gen-lang-client-0492208227'

      - name: Deploy Model
        run: |
          gcloud ai custom-jobs create \
            --region=us-central1 \
            --display-name="vertex-ai-deployment-job" \
            --python-package-uris="gs://cultragroundzero/training_script.py" \
            --python-module="main_script" \
            --args="--training_steps=1000,--learning_rate=0.001"
""")
print("GitHub Actions workflow created successfully.")
