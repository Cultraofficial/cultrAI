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

# Keep track of processed files by checking for "processed_" prefix
processed_prefix = "processed_"

# Download and process each file in the bucket
for blob in bucket.list_blobs(prefix=folder_path):
    filename = blob.name.split('/')[-1]
    local_path = os.path.join(local_directory, filename)

    # Skip files that are already processed (look for the "processed_" prefix)
    if filename.startswith(processed_prefix):
        print(f"Skipping already processed file: {filename}")
        continue

    # Download file
    blob.download_to_filename(local_path)
    print(f"Downloaded {blob.name} to {local_path}")

    # Process notebooks
    if local_path.endswith('.ipynb'):
        print(f"Executing notebook: {local_path}")
        with open(local_path) as f:
            nb = nbformat.read(f, as_version=4)

        # Execute with a timeout for each cell
        ep = ExecutePreprocessor(timeout=120, kernel_name='python3')  # Timeout set to 120 seconds
        try:
            ep.preprocess(nb, {'metadata': {'path': local_directory}})
            with open(local_path, 'w') as f:
                nbformat.write(nb, f)
            print(f"Executed notebook successfully: {local_path}")

            # Rename the file to mark it as processed
            processed_path = os.path.join(local_directory, processed_prefix + filename)
            os.rename(local_path, processed_path)
            print(f"Renamed to mark as processed: {processed_path}")

        except Exception as e:
            print(f"Error executing {local_path}: {e}")

print("All files processed.")
