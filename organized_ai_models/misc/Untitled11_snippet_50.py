def deploy_t5_xxl():
    model_display_name = "t5_xxl_model"
    model_path = "gs://cultra_official/models/t5_xxl"

    # Deploy T5-XXL to Vertex AI
    print("Deploying T5-XXL to Vertex AI...")
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
    print(f"T5-XXL model deployed to endpoint: {endpoint.resource_name}")

# Run deployment
deploy_t5_xxl()
