# Check for running training jobs
def check_training_jobs():
    print("Checking active training jobs...")
    jobs = aiplatform.CustomJob.list()
    if not jobs:
        print("No active training jobs found.")
    else:
        for job in jobs:
            print(f"Training Job: {job.display_name}, State: {job.state}")
            if job.state != "JOB_STATE_SUCCEEDED":
                print(f"Consider cancelling training job: {job.display_name}")

# Check for active pipelines
def check_pipelines():
    print("Checking active pipelines...")
    pipelines = aiplatform.PipelineJob.list()
    if not pipelines:
        print("No active pipelines found.")
    else:
        for pipeline in pipelines:
            print(f"Pipeline: {pipeline.display_name}, State: {pipeline.state}")
            if pipeline.state == "PIPELINE_STATE_RUNNING":
                print(f"Consider pausing pipeline: {pipeline.display_name}")

# Main workflow to check all resources
def check_all_resources():
    check_training_jobs()
    check_pipelines()

check_all_resources()
