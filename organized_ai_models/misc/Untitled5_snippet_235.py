# Specify the Docker image for deployment
container_image = "us-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.1-12:latest"  # Updated image to avoid errors

# Upload and deploy the model to an endpoint on Vertex AI
model = aiplatform.Model.upload(
    display_name="huggingface-model",
    artifact_uri=f"gs://{bucket_name}/models/",
    serving_container_image_uri=container_image,
)

# Create and deploy the model to an endpoint
endpoint = model.deploy(
    machine_type="n1-standard-4",
    min_replica_count=1,
    max_replica_count=2,
)

print("Model deployed on Google Vertex AI.")
