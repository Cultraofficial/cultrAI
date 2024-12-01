# Install the transformers library if not already installed
!pip install transformers

# Import necessary modules
from transformers import AutoModel, AutoTokenizer
import os
import torch

# Mount Google Drive (re-mount for a fresh session)
from google.colab import drive
drive.mount('/content/drive')

# Set the Hugging Face authentication token
os.environ["HUGGING_FACE_TOKEN"] = "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"

# Define the save path in Google Drive
save_path = "/content/drive/My Drive/Colab_models/"

# List of the next 25 models to download - make sure these are correct and do not require replacements
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
    "EleutherAI/gpt-neo-1.3B",
    "facebook/opt-1.3b",
    "EleutherAI/gpt-neo-2.7B",
    "facebook/bart-large-xsum",
    "facebook/opt-2.7b",
    "Salesforce/codegen-350M-mono",
    "microsoft/DialoGPT-medium",
    "facebook/bart-large-mnli",
    "openai/whisper-base",
    "facebook/opt-6.7b",
    "EleutherAI/gpt-j-6B",
    "bigscience/bloom-560m",
    "google/t5-11b",
    "facebook/opt-30b",
    "stabilityai/stablelm-base-alpha-7b",
    "EleutherAI/gpt-j-8B-finetuned"
]

# Function to download and save a model
def download_and_save_model(model_name, token=os.getenv("HUGGING_FACE_TOKEN")):
    print(f"Starting download for model: {model_name}")
    try:
        # Load model and tokenizer
        model = AutoModel.from_pretrained(model_name, token=token)
        tokenizer = AutoTokenizer.from_pretrained(model_name, token=token)

        # Save model and tokenizer to Google Drive
        model.save_pretrained(f"{save_path}{model_name}")
        tokenizer.save_pretrained(f"{save_path}{model_name}")

        print(f"Downloaded and saved: {model_name}")

        # Clear model from memory
        del model
        del tokenizer
        torch.cuda.empty_cache()  # Clears any GPU memory if available

    except Exception as e:
        print(f"Failed to download {model_name}. Error: {e}")

# Download each model in the list
for model_name in models_to_download:
    download_and_save_model(model_name)
