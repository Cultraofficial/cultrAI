import os
from transformers import AutoModel, AutoTokenizer
from huggingface_hub import login
import torch

# Automatically use one of the provided Hugging Face tokens
HUGGING_FACE_TOKEN = "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"  # Newest token

# Authenticate with Hugging Face
login(HUGGING_FACE_TOKEN)

# Directory to save models
target_dir = "/content/drive/My Drive/Colab_models"
os.makedirs(target_dir, exist_ok=True)

# Define additional models to download
models_to_download = [
    "bigscience/bloom-176b",
    "EleutherAI/gpt-j-6B",
    "facebook/opt-66b",
    "mistralai/Mistral-7B-v0.1",
    "h2oai/h2ogpt-oig-oasst1-256-12b",
    # Add more models as needed
]

# Function to clear memory and download each model
def download_model(model_name):
    print(f"Attempting to download {model_name}...")
    try:
        # Load model and tokenizer
        model = AutoModel.from_pretrained(model_name, cache_dir=target_dir, use_auth_token=HUGGING_FACE_TOKEN)
        tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=target_dir, use_auth_token=HUGGING_FACE_TOKEN)
        print(f"Successfully downloaded and saved {model_name}.")

        # Clear memory after each download
        del model, tokenizer
        torch.cuda.empty_cache()
    except Exception as e:
        print(f"Failed to download {model_name}: {e}")

# Download each model
for model_name in models_to_download:
    download_model(model_name)
