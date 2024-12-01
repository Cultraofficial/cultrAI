def cleanup_vertex_ai_resources():
    try:
        jobs = aiplatform.CustomJob.list()
        for job in jobs:
            if job.state.name not in ["SUCCEEDED", "FAILED"]:
                print(f"Cancelling job: {job.display_name}")
                job.cancel()

        endpoints = aiplatform.Endpoint.list()
        for endpoint in endpoints:
            print(f"Deactivating endpoint: {endpoint.display_name}")
            endpoint.undeploy_all()
    except Exception as e:
        print(f"Failed to clean up Vertex AI resources: {e}")

cleanup_vertex_ai_resources()
