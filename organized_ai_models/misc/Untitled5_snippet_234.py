import os

model_path = "/content/model"

for file_name in os.listdir(model_path):
    blob = bucket.blob(f"models/{file_name}")
    blob.upload_from_filename(os.path.join(model_path, file_name))
print("Model uploaded to Google Cloud Storage.")
