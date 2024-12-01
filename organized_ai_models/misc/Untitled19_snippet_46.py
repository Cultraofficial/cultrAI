# Install necessary libraries
!pip install google-cloud-aiplatform google-cloud-storage --quiet

# Import required libraries
from google.cloud import aiplatform, storage
import os
from google.colab import drive

# Mount Google Drive to access your service account key
drive.mount('/content/drive')

# Path to your service account key JSON file
SERVICE_ACCOUNT_KEY = "/content/drive/My Drive/BrandNewKey.json"  # Update path if needed

# Authenticate with Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY
print("Authenticated with the service account.")

# Initialize Vertex AI
aiplatform.init(project="gen-lang-client-0492208227", location="us-central1")

# Function to list and stop unnecessary endpoints
def stop_unused_endpoints():
    print("Checking active endpoints...")
    endpoints = aiplatform.Endpoint.list()
    if not endpoints:
        print("No active endpoints found.")
        return

    for endpoint in endpoints:
        print(f"Endpoint: {endpoint.display_name}, Resource Name: {endpoint.resource_name}")
        if input(f"Pause {endpoint.display_name}? (yes/no): ").lower() == "yes":
            endpoint.undeploy_all()
            print(f"Paused endpoint: {endpoint.display_name}")
        else:
            print(f"Skipping: {endpoint.display_name}")

# Main workflow
def main():
    print("Starting Vertex AI troubleshooting...")
    stop_unused_endpoints()
    print("Completed troubleshooting.")

main()
