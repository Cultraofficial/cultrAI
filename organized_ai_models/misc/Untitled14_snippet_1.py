# Import required libraries
from huggingface_hub import hf_hub_download
import os

# Hugging Face token for authentication
token = "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"

# List of models that previously failed to download
failed_models = [
    "EleutherAI/gpt-neox-3B-finetuned",
    "microsoft/codex-cushman",
    "HuggingFace/transformerXL-large",
    "google/t5-3b",
    "openai/dall-e-mini",
    "facebook/opt-13b-finetuned",
    "facebook/fairseq-transformer",
    "google/t5-11b",
    "EleutherAI/gpt-j-8B-finetuned"
]

# Directory to save downloaded models in Google Drive
model_dir = "/content/drive/My Drive/colab_models"

# Ensure Google Drive is mounted
from google.colab import drive
drive.mount('/content/drive')

# Function to download files for each model
def download_model_files(model, files, token, model_dir):
    for file in files:
        try:
            # Download each file to its respective model folder
            hf_hub_download(repo_id=model, filename=file,
                            local_dir=os.path.join(model_dir, model.replace("/", "_")), token=token)
            print(f"{file} for {model} successfully saved to {os.path.join(model_dir, model.replace('/', '_'))}")
        except Exception as e:
            print(f"Failed to download {file} for {model}: {e}")

# List of files typically associated with each model
files_to_download = ["config.json", "pytorch_model.bin", "tokenizer.json", "vocab.json", "merges.txt"]

# Attempt to download each model
for model in failed_models:
    print(f"Downloading {model}...")
    download_model_files(model, files_to_download, token, model_dir)
    print(f"Finished downloading {model}\n")
