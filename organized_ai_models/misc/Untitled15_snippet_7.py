# Install necessary libraries if not already installed
!pip install transformers

# Import necessary modules
from transformers import AutoModel, AutoTokenizer
import os
import torch

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Define Hugging Face token
os.environ["HUGGING_FACE_TOKEN"] = "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"

# Google Drive save path
save_path = "/content/drive/My Drive/Colab_models/"

# List of models to download - make sure these are verified and copy-paste ready
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
    "EleutherAI/gpt-neo-1.3B",
    "google/pegasus-cnn-dailymail",
    "facebook/opt-1.3b",
    "EleutherAI/gpt-neo-2.7B",
    "facebook/bart-large-xsum",
    "facebook/opt-2.7b",
    "facebook/m2m100-418M",
    "Salesforce/codegen-350M-mono",
    "microsoft/DialoGPT-medium",
    "facebook/bart-large-mnli",
    "openai/whisper-base",
    "facebook/opt-6.7b",
    "EleutherAI/gpt-j-6B",
    "EleutherAI/gpt-neo-4.6B",
    "bigscience/bloom-560m"
]

# Function to download and save model to Google Drive
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

        # Clear model from memory to manage resources
        del model
        del tokenizer
        torch.cuda.empty_cache()  # Clears any GPU memory if available

    except Exception as e:
        print(f"Failed to download {model_name}. Error: {e}")

# Download the models
for model_name in models_to_download:
    download_and_save_model(model_name)
