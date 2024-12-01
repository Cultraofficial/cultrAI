def check_training_jobs():
    print("Listing all training jobs...")
    jobs = aiplatform.CustomJob.list()
    if not jobs:
        print("No training jobs found.")
    else:
        for job in jobs:
            print(f"Job: {job.display_name}, State: {job.state}")

check_training_jobs()
