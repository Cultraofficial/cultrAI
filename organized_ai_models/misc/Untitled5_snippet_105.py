# Initialize Vertex AI with the project ID and region
PROJECT_ID = "cultra-2ffad"  # Replace with your actual project ID if different
REGION = "us-central1"       # Set the desired region

aiplatform.init(project=PROJECT_ID, location=REGION)
print("Vertex AI initialized successfully.")
