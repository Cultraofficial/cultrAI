# Step 1: Import necessary libraries
import os
from google.colab import drive
from google.cloud import aiplatform

# Step 2: Mount Google Drive
drive.mount('/content/drive')

# Step 3: Set the Google Application Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"

# Step 4: Initialize AI Platform with project ID and location
aiplatform.init(project="gen-lang-client-0492208227", location="us-central1")

# Step 5: Test the setup by listing available models
models = aiplatform.Model.list()
print("Available models:", models)
