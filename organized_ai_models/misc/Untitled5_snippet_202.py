import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from google.cloud import storage

# Initialize Google Cloud Storage client with the service account
storage_client = storage.Client.from_service_account_json('/content/drive/My Drive/BrandNewKey.json')

# Define the bucket and folder path
bucket_name = 'cultra_official'
folder_path = 'platform/processed/'

# Connect to the bucket
bucket = storage_client.get_bucket(bucket_name)

# Local directory in Google Colab
local_directory = '/vertex_ai_workspace/'
os.makedirs(local_directory, exist_ok=True)

# Keep track of processed files to avoid reprocessing
processed_files = set()

# Download and process each file in the bucket
for blob in bucket.list_blobs(prefix=folder_path):
    filename = blob.name.split('/')[-1]
    local_path = os.path.join(local_directory, filename)

    # Only download and process if not already processed
    if filename not in processed_files:
        # Download file
        blob.download_to_filename(local_path)
        print(f"Downloaded {blob.name} to {local_path}")

        # Add to processed files list
        processed_files.add(filename)

        # Process notebooks
        if local_path.endswith('.ipynb'):
            print(f"Executing notebook: {local_path}")
            with open(local_path) as f:
                nb = nbformat.read(f, as_version=4)

            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            try:
                ep.preprocess(nb, {'metadata': {'path': local_directory}})
                with open(local_path, 'w') as f:
                    nbformat.write(nb, f)
                print(f"Executed notebook successfully: {local_path}")
            except Exception as e:
                print(f"Error executing {local_path}: {e}")
    else:
        print(f"Skipping already processed file: {filename}")

print("All files processed.")
