from google.cloud import aiplatform

# Initialize Vertex AI with project and location details
aiplatform.init(project="gen-lang-client-0492208227", location="us-central1")

# Upload model to Vertex AI and deploy
model = aiplatform.Model.upload(
    display_name="huggingface-model",
    artifact_uri=f"gs://{bucket_name}/models/",
    serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.1-7:latest",
)

# Deploy model to an endpoint
endpoint = model.deploy(
    machine_type="n1-standard-4",
    min_replica_count=1,
    max_replica_count=2,
)
print("Model deployed on Google Vertex AI.")
