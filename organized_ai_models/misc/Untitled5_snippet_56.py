from google.cloud import aiplatform

# Initialize Vertex AI
project_id = "gen-lang-client-0492208227"
region = "us-central1"  # Adjust as needed

aiplatform.init(project=project_id, location=region)
print("Vertex AI initialized successfully.")
