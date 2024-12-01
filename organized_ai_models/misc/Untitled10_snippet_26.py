storage_client = storage.Client(credentials=credentials)
bucket_name = "cultragroundzero"
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob("training_script.py")
blob.upload_from_filename("main_script.py")

print("Training script uploaded to:", f"gs://{bucket_name}/training_script.py")
