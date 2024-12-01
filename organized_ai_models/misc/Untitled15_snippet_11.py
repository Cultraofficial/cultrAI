# Install necessary libraries
!pip install transformers

# Import necessary modules
import os
from transformers import AutoModel, AutoTokenizer
import torch

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Define Hugging Face tokens and set the latest as default
os.environ["HUGGING_FACE_TOKEN"] = "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"

# Google Drive save path
save_path = "/content/drive/My Drive/Colab_models/"

# List of models to download, ordered from smallest to largest
models_to_download = [
    "distilgpt2",
    "distilroberta-base",
    "cardiffnlp/twitter-roberta-base-sentiment",
    "EleutherAI/gpt-neo-125M",
    "deepset/roberta-base-squad2",
    "microsoft/codebert-base-mlm",
    "allenai/longformer-base-4096",
    "sentence-transformers/all-MiniLM-L6-v2",
    "facebook/bart-large-cnn",
    "google/t5-small",
    "AdapterHub",
    "BioBERT",
    "Polyglot-Ko-12.8B",
    "DeepMind MuZero",
    "DeepMind AlphaCode",
    "EleutherAI/gpt-neo-1.3B",
    "google/pegasus-cnn-dailymail",
    "SpatioTemporal Asset Catalog (STAC)",
    "facebook/opt-1.3b",
    "EleutherAI/gpt-neo-2.7B",
    "DreamFusion",
    "Salesforce/codegen-350M-mono",
    "microsoft/DialoGPT-medium",
    "ControlNet",
    "facebook/bart-large-mnli",
    # Add the remaining models in your list as needed
]

# Function to download and save model
def download_and_save_model(model_name, token=os.getenv("HUGGING_FACE_TOKEN")):
    print(f"Starting download for model: {model_name}")
    try:
        # Load model and tokenizer
        model = AutoModel.from_pretrained(model_name, use_auth_token=token)
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)

        # Save model and tokenizer to Google Drive
        model.save_pretrained(f"{save_path}{model_name}")
        tokenizer.save_pretrained(f"{save_path}{model_name}")

        print(f"Downloaded and saved: {model_name}")

        # Clear model from memory
        del model
        del tokenizer
        torch.cuda.empty_cache()  # Clears GPU memory if available

    except Exception as e:
        print(f"Failed to download {model_name}. Error: {e}")

# Download models in batches of 25 to manage memory
batch_size = 25
for i in range(0, len(models_to_download), batch_size):
    batch = models_to_download[i:i + batch_size]
    for model_name in batch:
        download_and_save_model(model_name)

    # Clear cache between batches
    torch.cuda.empty_cache()
