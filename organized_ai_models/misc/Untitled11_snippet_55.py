from google.cloud import storage

# Initialize Google Cloud Storage client
project_id = "gen-lang-client-0492208227"
bucket_name = "cultra_official"
storage_client = storage.Client(project=project_id)
bucket = storage_client.bucket(bucket_name)

def check_and_log_model_files(model_name):
    # Set up the prefix for the model path in Cloud Storage
    prefix = f"models/{model_name}"
    print(f"\nChecking contents of gs://{bucket_name}/{prefix}...")

    # List blobs (files) in the specified model directory
    blobs = list(bucket.list_blobs(prefix=prefix))

    if blobs:
        print(f"Files found for model '{model_name}':")
        for blob in blobs:
            print(f" - {blob.name} (Size: {blob.size} bytes)")
    else:
        print(f"No files found in 'gs://{bucket_name}/{prefix}'. Please upload the model files if not present.")

# List of model directories to check
model_names = ["bloom", "falcon", "llama", "distilbert", "gpt_neo", "t5_xxl"]

# Run the check for each model
for model in model_names:
    check_and_log_model_files(model)
