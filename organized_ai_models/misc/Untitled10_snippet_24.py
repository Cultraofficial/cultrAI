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
      uses: google-github-actions/setup-gcloud@v0.2.0
      with:
        project_id: gen-lang-client-0492208227
        service_account_key: ${{ secrets.GOOGLE_APPLICATION_CREDENTIALS }}
        export_default_credentials: true

    - name: Deploy Model
      run: |
        gcloud ai custom-jobs create \
          --region=us-central1 \
          --display-name="vertex-ai-deployment-job" \
          --python-package-uris="gs://cultragroundzero/training_script.py" \
          --python-module="main_script" \
          --args="--training_steps=1000,--learning_rate=0.001"
"""

# Write the workflow file
os.makedirs(".github/workflows", exist_ok=True)
with open(".github/workflows/deploy-to-vertex-ai.yml", "w") as file:
    file.write(workflow_content)
