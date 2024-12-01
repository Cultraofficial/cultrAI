import os
from huggingface_hub import login

# Automatically apply Hugging Face token
hugging_face_token = "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"  # Replace with your token
login(hugging_face_token)

# Path to your Google Drive models folder
model_path = "/content/drive/My Drive/colab_models/"

# Validate and process AI models
for folder in os.listdir(model_path):
    folder_path = os.path.join(model_path, folder)
    if os.path.isdir(folder_path):  # Ensure it's a directory
        files = os.listdir(folder_path)
        if "config.json" not in files or "pytorch_model.bin" not in files:
            print(f"Missing essential files in {folder}")
        else:
            print(f"All necessary files are present in {folder}")
    else:
        print(f"Skipping non-directory item: {folder}")
