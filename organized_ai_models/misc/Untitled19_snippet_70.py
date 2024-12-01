from google.cloud import aiplatform

# Initialize Vertex AI
aiplatform.init(project="gen-lang-client-0492208227", location="us-central1")

# Delete Completed Training Jobs
def delete_completed_training_jobs():
    jobs = aiplatform.CustomJob.list()
    for job in jobs:
        if job.state in ["JOB_STATE_SUCCEEDED", "JOB_STATE_FAILED"]:
            print(f"Deleting completed job: {job.display_name}")
            job.delete()
            print(f"Deleted job: {job.display_name}")

delete_completed_training_jobs()
