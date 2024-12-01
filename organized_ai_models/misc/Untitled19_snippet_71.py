def list_unused_resources():
    print("Checking for unused endpoints, training jobs, or batch predictions...")
    endpoints = aiplatform.Endpoint.list()
    for endpoint in endpoints:
        print(f"Endpoint: {endpoint.display_name}, Resource Name: {endpoint.resource_name}")

    jobs = aiplatform.CustomJob.list()
    for job in jobs:
        print(f"Training Job: {job.display_name}, State: {job.state}, Resource Name: {job.resource_name}")

    batch_predictions = aiplatform.BatchPredictionJob.list()
    for prediction in batch_predictions:
        print(f"Batch Prediction: {prediction.display_name}, State: {prediction.state}, Resource Name: {prediction.resource_name}")

list_unused_resources()
