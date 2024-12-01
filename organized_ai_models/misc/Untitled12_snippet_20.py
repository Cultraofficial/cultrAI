import os

# Set the path to your Google Drive ModelStorage folder
model_storage_path = '/content/drive/My Drive/ModelStorage/'

# List all the folders (models) in ModelStorage directory
if os.path.exists(model_storage_path):
    uploaded_models = os.listdir(model_storage_path)
    print("Models already uploaded to Google Drive:")
    for model in uploaded_models:
        print("-", model)
else:
    print("ModelStorage folder does not exist. Please make sure the path is correct.")
