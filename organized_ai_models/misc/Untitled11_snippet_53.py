def deploy_gpt_neo():
    model_display_name = "gpt_neo_model"
    model_path = "gs://cultra_official/models/gpt_neo"

    # Deploy GPT-Neo to Vertex AI
    print("Deploying GPT-Neo to Vertex AI...")
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
    print(f"GPT-Neo model deployed to endpoint: {endpoint.resource_name}")

# Run deployment
deploy_gpt_neo()
