# Install necessary libraries
!pip install transformers

# Import necessary modules
from transformers import AutoModel, AutoTokenizer
import os
import torch
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Define Hugging Face tokens and automatically set the latest token as default
os.environ["HUGGING_FACE_TOKEN"] = "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"

# Google Drive save path
save_path = "/content/drive/My Drive/Colab_models/"

# List of the next 25 models to download, ordered from smallest to largest
models_to_download = [
    "model_26_name", "model_27_name", "model_28_name", "model_29_name", "model_30_name",
    "model_31_name", "model_32_name", "model_33_name", "model_34_name", "model_35_name",
    "model_36_name", "model_37_name", "model_38_name", "model_39_name", "model_40_name",
    "model_41_name", "model_42_name", "model_43_name", "model_44_name", "model_45_name",
    "model_46_name", "model_47_name", "model_48_name", "model_49_name", "model_50_name"
]

# Function to download and save each model to the designated Google Drive folder
def download_and_save_model(model_name):
    print(f"Starting download for model: {model_name}")
    try:
        # Load model and tokenizer with Hugging Face token
        model = AutoModel.from_pretrained(model_name, token=os.getenv("HUGGING_FACE_TOKEN"))
        tokenizer = AutoTokenizer.from_pretrained(model_name, token=os.getenv("HUGGING_FACE_TOKEN"))

        # Save model and tokenizer to Google Drive
        model.save_pretrained(f"{save_path}{model_name}")
        tokenizer.save_pretrained(f"{save_path}{model_name}")

        print(f"Downloaded and saved: {model_name}")

        # Clear model from memory to manage resources
        del model
        del tokenizer
        torch.cuda.empty_cache()  # Clears GPU memory if available

    except Exception as e:
        print(f"Failed to download {model_name}. Error: {e}")

# Download models in this batch of 25
for model_name in models_to_download:
    download_and_save_model(model_name)

# Clear cache at the end
torch.cuda.empty_cache()
