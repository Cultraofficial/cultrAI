from google.cloud import aiplatform

# Initialize AI Platform
aiplatform.init(project="gen-lang-client-0492208227", location="us-central1")

# List and delete completed jobs
def delete_completed_jobs():
    jobs = aiplatform.CustomJob.list()
    for job in jobs:
        if job.state == "JOB_STATE_SUCCEEDED":
            print(f"Deleting completed job: {job.display_name}")
            job.delete()
    print("Completed jobs deleted.")

delete_completed_jobs()
