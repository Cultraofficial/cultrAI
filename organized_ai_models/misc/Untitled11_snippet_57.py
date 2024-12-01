from google.cloud import storage

def move_files_to_model_directory(model_name, files):
    # Set up Google Cloud Storage client and bucket
    project_id = "gen-lang-client-0492208227"
    bucket_name = "cultra_official"
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)

    # Define target directory
    target_prefix = f"models/{model_name}/"

    # Move each file to the new model directory
    for file in files:
        source_blob = bucket.blob(file)
        target_blob = bucket.blob(target_prefix + file.split('/')[-1])
        bucket.copy_blob(source_blob, bucket, target_blob.name)
        source_blob.delete()  # Optionally delete the old file
        print(f"Moved {file} to {target_blob.name}")

# List of files currently under `models/` to move
files_to_move = [
    "models/config.json",
    "models/model.safetensors",
    "models/special_tokens_map.json",
    "models/tokenizer.json",
    "models/tokenizer_config.json",
    "models/vocab.txt"
]

# Move files to 'bloom' directory
move_files_to_model_directory("bloom", files_to_move)
