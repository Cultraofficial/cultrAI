# Upload processed notebooks back to Google Cloud Storage
for filename in os.listdir(local_directory):
    local_path = os.path.join(local_directory, filename)
    remote_path = folder_path + "processed/" + filename  # Adjust folder structure as needed

    # Upload file
    blob = bucket.blob(remote_path)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {filename} to {remote_path}")
