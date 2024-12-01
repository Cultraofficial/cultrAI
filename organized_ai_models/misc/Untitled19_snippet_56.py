def check_all_training_jobs():
    print("Checking all training jobs...")
    jobs = aiplatform.CustomJob.list()
    if not jobs:
        print("No active training jobs found.")
    else:
        for job in jobs:
            print(f"Training Job: {job.display_name}, State: {job.state}")

check_all_training_jobs()
