from google.cloud import storage

bucket_name = "cultra_official"
model_path = "/content/model"
mar_file = f"{model_name}.mar"

# Initialize Google Cloud Storage client
storage_client = storage.Client(project="gen-lang-client-0492208227")
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(f"models/{mar_file}")
blob.upload_from_filename(os.path.join(model_path, mar_file))

print(f"Model .mar file uploaded to gs://{bucket_name}/models/{mar_file}")
