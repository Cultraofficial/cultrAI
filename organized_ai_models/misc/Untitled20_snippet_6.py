import os
import shutil
from huggingface_hub import HfApi, HfFolder, login

# Authenticate Hugging Face
hugging_face_token = "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"
login(hugging_face_token)

# Paths
model_path = "/content/drive/My Drive/colab_models/"
missing_files_path = os.path.join(model_path, "missing_files")
complete_models_path = os.path.join(model_path, "complete_models")
misc_files_path = os.path.join(model_path, "misc_files")

# Create directories for organizing
os.makedirs(missing_files_path, exist_ok=True)
os.makedirs(complete_models_path, exist_ok=True)
os.makedirs(misc_files_path, exist_ok=True)

# Initialize Hugging Face API
hf_api = HfApi()

# Iterate through folders and validate
for folder in os.listdir(model_path):
    folder_path = os.path.join(model_path, folder)

    # Skip non-directory items
    if not os.path.isdir(folder_path):
        print(f"Moving non-directory item to misc_files: {folder}")
        shutil.move(folder_path, os.path.join(misc_files_path, folder))
        continue

    # Check for essential files
    files = os.listdir(folder_path)
    if "config.json" in files and "pytorch_model.bin" in files:
        print(f"✅ All necessary files are present in {folder}. Moving to complete_models.")
        shutil.move(folder_path, os.path.join(complete_models_path, folder))
    else:
        print(f"❌ Missing essential files in {folder}. Moving to missing_files.")
        shutil.move(folder_path, os.path.join(missing_files_path, folder))

# Download missing files for models in missing_files
for folder in os.listdir(missing_files_path):
    folder_path = os.path.join(missing_files_path, folder)
    try:
        print(f"🔄 Attempting to download missing files for {folder}...")
        hf_api.download_repo(folder_id=folder, repo_type="model", local_dir=folder_path, use_auth_token=hugging_face_token)
        print(f"✅ Successfully downloaded missing files for {folder}.")
        shutil.move(folder_path, os.path.join(complete_models_path, folder))
    except Exception as e:
        print(f"❌ Failed to download missing files for {folder}: {e}")
