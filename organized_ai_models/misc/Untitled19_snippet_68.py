def cancel_batch_predictions():
    batch_predictions = aiplatform.BatchPredictionJob.list()
    for prediction in batch_predictions:
        if prediction.state in ["JOB_STATE_RUNNING", "JOB_STATE_PENDING"]:
            print(f"Cancelling batch prediction: {prediction.display_name}")
            prediction.cancel()
            print(f"Cancelled batch prediction: {prediction.display_name}")

cancel_batch_predictions()
