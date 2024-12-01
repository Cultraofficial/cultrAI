from google.cloud import aiplatform, storage
import os

# Initialize Vertex AI
aiplatform.init(project="gen-lang-client-0492208227", location="us-central1")

# Initialize Google Cloud Storage client
storage_client = storage.Client(project="gen-lang-client-0492208227")
bucket_name = "cultragroundzero"
bucket = storage_client.bucket(bucket_name)

# List models in the Google Cloud Storage bucket
blobs = bucket.list_blobs(prefix="models/")
model_paths = [blob.name for blob in blobs if blob.name.endswith(".zip")]

# Deploy models to Vertex AI
for model_path in model_paths:
    model_display_name = os.path.basename(model_path).replace(".zip", "")
    model = aiplatform.Model.upload(
        display_name=model_display_name,
        artifact_uri=f"gs://{bucket_name}/{model_path}",
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-5:latest",  # Replace with your specific container if needed
    )
    endpoint = model.deploy(machine_type="n1-standard-4")
    print(f"Deployed model '{model_display_name}' at endpoint: {endpoint.resource_name}")
