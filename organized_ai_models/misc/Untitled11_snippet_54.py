import os

# Function to upload local files to a specified Cloud Storage directory
def upload_model_files(local_model_path, model_name):
    gcs_model_path = f"models/{model_name}"
    bucket = storage_client.bucket(bucket_name)

    # Upload files in the specified local path
    for root, _, files in os.walk(local_model_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            destination_blob_path = os.path.join(gcs_model_path, os.path.relpath(local_file_path, local_model_path))
            blob = bucket.blob(destination_blob_path)
            blob.upload_from_filename(local_file_path)
            print(f"Uploaded {local_file_path} to gs://{bucket_name}/{destination_blob_path}")

# Example usage (update the local paths with your own paths)
upload_model_files("/path/to/local/bloom", "bloom")
upload_model_files("/path/to/local/falcon", "falcon")
upload_model_files("/path/to/local/llama", "llama")
upload_model_files("/path/to/local/distilbert", "distilbert")
upload_model_files("/path/to/local/gpt_neo", "gpt_neo")
upload_model_files("/path/to/local/t5_xxl", "t5_xxl")
