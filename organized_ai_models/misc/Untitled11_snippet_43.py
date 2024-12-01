def deploy_bloom():
    model_display_name = "bloom_model"
    model_path = "gs://cultra_official/models/bloom"

    # Upload the model if not already in GCS
    if not bucket.blob("models/bloom").exists():
        # Add code here to upload BLOOM model to GCS
        print("Uploading BLOOM model to Google Cloud Storage...")

    # Deploy model to Vertex AI
    print("Deploying BLOOM to Vertex AI...")
    model = aiplatform.Model.upload(
        display_name=model_display_name,
        artifact_uri=model_path,
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.1-7:latest"
    )
    endpoint = model.deploy(
        machine_type="n1-standard-4",
        min_replica_count=1,
        max_replica_count=3,
    )
    print(f"BLOOM model deployed to endpoint: {endpoint.resource_name}")

# Run deployment
deploy_bloom()
