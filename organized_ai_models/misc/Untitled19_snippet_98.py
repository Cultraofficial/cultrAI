def cleanup_vertex_ai_resources():
    print("Cleaning up Vertex AI resources...")

    # Delete Endpoints
    endpoints = aiplatform.Endpoint.list()
    for endpoint in endpoints:
        print(f"Deleting endpoint: {endpoint.display_name}")
        endpoint.delete()

    # Cancel Training Jobs
    jobs = aiplatform.CustomJob.list()
    for job in jobs:
        if job.state not in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            print(f"Cancelling training job: {job.display_name}")
            job.cancel()

    # Delete Pipelines
    pipelines = aiplatform.PipelineJob.list()
    for pipeline in pipelines:
        if pipeline.state not in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            print(f"Cancelling pipeline: {pipeline.display_name}")
            pipeline.cancel()

    # Cancel Batch Predictions
    batch_predictions = aiplatform.BatchPredictionJob.list()
    for batch in batch_predictions:
        if batch.state not in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            print(f"Cancelling batch prediction: {batch.display_name}")
            batch.cancel()

    print("Cleanup complete.")

cleanup_vertex_ai_resources()
