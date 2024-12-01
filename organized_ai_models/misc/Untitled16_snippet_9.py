from transformers import AutoModel, AutoTokenizer
import os

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Set the path to save models in Google Drive
save_path = "/content/drive/My Drive/Colab_models/"

# List of the first 25 models to download
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
    "facebook/opt-1.3b",
    "EleutherAI/gpt-neo-2.7B",
    "facebook/bart-large-xsum",
    "facebook/opt-2.7b",
    "Salesforce/codegen-350M-mono",
    "microsoft/DialoGPT-medium",
    "facebook/bart-large-mnli",
    "openai/whisper-base",
    "bigscience/bloom-560m",
    "facebook/opt-6.7b",
    "EleutherAI/gpt-j-6B",
    "EleutherAI/gpt-neo-4.6B",
    "bigscience/T0_3B",
    "facebook/opt-13b"
]

# Function to download and save models
def download_model(model_name):
    try:
        model = AutoModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model.save_pretrained(os.path.join(save_path, model_name.replace("/", "_")))
        tokenizer.save_pretrained(os.path.join(save_path, model_name.replace("/", "_")))
        print(f"Downloaded and saved: {model_name}")
    except Exception as e:
        print(f"Failed to download {model_name}. Error: {str(e)}")

# Download each model in the list
for model_name in models_to_download:
    download_model(model_name)

print("Download process completed. Check your Google Drive for saved models.")
