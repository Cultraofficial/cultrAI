from google.cloud import storage
import os

# Apply Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"  # Ensure path accuracy

# Initialize Google Cloud Storage client with project details
client = storage.Client(project="gen-lang-client-0492208227")
bucket_name = "cultra_official"
bucket = client.get_bucket(bucket_name)

# Upload the model files to the specified bucket
model_path = "/content/model"
for file_name in os.listdir(model_path):
    blob = bucket.blob(f"models/{file_name}")
    blob.upload_from_filename(os.path.join(model_path, file_name))
    print(f"Uploaded {file_name} to gs://{bucket_name}/models/")
