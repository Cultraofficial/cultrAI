from google.colab import drive
from transformers import AutoModel, AutoTokenizer
import os
import gc
from huggingface_hub import login

# Mount Google Drive
drive.mount("/content/drive", force_remount=True)

# Hugging Face Token Authentication
huggingface_token_1 = "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"
huggingface_token_2 = "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"
login(token=huggingface_token_1)  # Use your Hugging Face tokens

# Directory to store models
model_directory = "/content/drive/My Drive/colab_models"

# List of models to download
models_to_download = [
    "EleutherAI/gpt-neo-2.7B", "EleutherAI/gpt-neo-1.3B", "bigscience/bloom-560m",
    "facebook/bart-large-cnn", "google/flan-t5-xxl", "bert-base-uncased",
    "microsoft/codebert-base-mlm", "facebook/opt-13b", "EleutherAI/gpt-j-6B"
]  # Add all other model names as required

# Function to download and save models
def download_model(model_name, save_path):
    try:
        print(f"Downloading {model_name}...")
        model = AutoModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model.save_pretrained(save_path)
        tokenizer.save_pretrained(save_path)
        print(f"Model {model_name} saved to {save_path}")
    except Exception as e:
        print(f"Failed to download {model_name}: {e}")

# Function to clear memory and disk space
def clear_space():
    print("Clearing memory and disk space...")
    gc.collect()
    os.system("sync")
    # You can also use os.system("rm -rf /content/drive/My Drive/colab_models/temp/*") if you have temporary files

# Loop through the model list
for model_name in models_to_download:
    # Generate save path
    save_path = model_directory + model_name.split("/")[-1]  # Save in colab_models directory
    download_model(model_name, save_path)
    clear_space()  # Clear space after each model download

