# Define the path to the script or model you want to deploy
script_path = "gs://cultragroundzero/your_repo_name/your_script.py"  # Adjust as needed

# Submit the custom job to Vertex AI
job = aiplatform.CustomJob.from_local_script(
    display_name="vertex-ai-deployment-job",
    script_path=script_path,
    container_uri="gcr.io/deeplearning-platform-release/tf2-cpu.2-3:latest",
    project=project_id,
    location="us-central1",
    staging_bucket=bucket_name,
    credentials=credentials
)

# Run the job
job.run(sync=False)
print("Job submitted. Monitor it in the Google Cloud Console.")
