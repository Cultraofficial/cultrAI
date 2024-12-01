def delete_training_jobs():
    print("Deleting completed training jobs...")
    jobs = aiplatform.CustomJob.list()
    for job in jobs:
        if job.state == "JOB_STATE_SUCCEEDED":
            print(f"Deleting job: {job.display_name}")
            job.delete()
            print(f"Deleted job: {job.display_name}")

delete_training_jobs()
