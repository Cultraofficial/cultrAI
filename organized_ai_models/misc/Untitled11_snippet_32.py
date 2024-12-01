# Import necessary libraries
from google.auth import default
from google.cloud import aiplatform
from google.cloud import storage
from google.api_core.exceptions import GoogleAPICallError, NotFound

# Define the project ID and bucket name
project_id = "gen-lang-client-0492208227"  # Explicitly specify the project ID
bucket_name = "cultragroundzero"  # Automatically applied bucket name

# Authenticate and set up Google Cloud project
try:
    credentials, _ = default()
    print(f"Authenticated successfully. Using project: {project_id}")
except Exception as e:
    print("Authentication failed:", e)

# Initialize Vertex AI client with the specified project ID
try:
    aiplatform.init(project=project_id, credentials=credentials)
    print("Vertex AI initialized successfully.")
except GoogleAPICallError as e:
    print("Failed to initialize Vertex AI:", e)

# Verify access to Google Cloud Storage
try:
    storage_client = storage.Client(project=project_id, credentials=credentials)
    buckets = list(storage_client.list_buckets())
    if any(bucket.name == bucket_name for bucket in buckets):
        print(f"Access to bucket '{bucket_name}' confirmed.")
    else:
        print(f"Bucket '{bucket_name}' not found.")
except GoogleAPICallError as e:
    print("Error accessing Google Cloud Storage:", e)

# List models in Vertex AI (to verify access to Vertex AI resources)
try:
    models = aiplatform.Model.list()
    if models:
        print("Models available in Vertex AI:")
        for model in models:
            print(f"- {model.display_name} (ID: {model.resource_name})")
    else:
        print("No models found in Vertex AI.")
except GoogleAPICallError as e:
    print("Error accessing Vertex AI models:", e)
except NotFound:
    print("No Vertex AI models found.")
