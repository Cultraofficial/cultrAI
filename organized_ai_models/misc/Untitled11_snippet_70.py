from google.cloud import aiplatform

# Initialize Vertex AI
project_id = "gen-lang-client-0492208227"
location = "us-central1"
bucket_name = "cultragroundzero"
model_file = "aiplatform-2024-11-16-22:03:42.415-aiplatform_custom_trainer_script-0.1.tar.gz"  # Update if needed

# Initialize the AI Platform
aiplatform.init(project=project_id, location=location)

# Path to model artifact in Google Cloud Storage
model_path = f"gs://{bucket_name}/{model_file}"

# Deploy the model
model = aiplatform.Model.upload(
    display_name="my_model",
    artifact_uri=model_path,
    serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-3:latest",
)

# Wait for deployment and print confirmation
model.wait()
print(f"Model deployed with ID: {model.resource_name}")
