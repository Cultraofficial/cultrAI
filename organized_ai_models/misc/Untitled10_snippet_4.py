# Initialize Vertex AI API Client using Service Account and Staging Bucket in the `us` location
aiplatform.init(
    project=project_id,
    location="us",  # Match this to the bucket's location
    credentials=credentials,
    staging_bucket=staging_bucket
)
