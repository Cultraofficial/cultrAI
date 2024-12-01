def cancel_training_jobs():
    print("Checking and cancelling active training jobs...")
    jobs = aiplatform.CustomJob.list()
    for job in jobs:
        if job.state not in ["JOB_STATE_SUCCEEDED", "JOB_STATE_CANCELLED", "JOB_STATE_FAILED"]:
            print(f"Cancelling job: {job.display_name}")
            job.cancel()
            print(f"Cancelled job: {job.display_name}")
        else:
            print(f"Job {job.display_name} is already completed or cancelled.")

cancel_training_jobs()
