from google.cloud import aiplatform

# Authenticate and initialize AI Platform
aiplatform.init(project="gen-lang-client-0492208227", location="us-central1")

def check_completed_jobs():
    print("Listing all training jobs and their states...")
    jobs = aiplatform.CustomJob.list()
    for job in jobs:
        print(f"Job: {job.display_name}, State: {job.state}, Create Time: {job.create_time}, Update Time: {job.update_time}")

check_completed_jobs()
