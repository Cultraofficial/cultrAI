# Import necessary libraries
import os
from transformers import AutoModel, AutoTokenizer
from huggingface_hub import login

# Authenticate with Hugging Face
login("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")

# Define the project folder in Google Drive and the list of models
project_folder = '/content/drive/My Drive/colab_models'
models = [
    "EleutherAI/gpt-neo-1.3B",
    "facebook/bart-large",
    "Salesforce/codegen-2B",
    "EleutherAI/gpt-neo-2.7B",
    "facebook/opt-2.7b"
]

# Download each model and save it to Google Drive
for model_name in models:
    try:
        print(f"Downloading {model_name}...")
        model = AutoModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Create a directory for each model and save
        model_dir = f"{project_folder}/{model_name.replace('/', '_')}"
        os.makedirs(model_dir, exist_ok=True)

        model.save_pretrained(model_dir)
        tokenizer.save_pretrained(model_dir)

        print(f"{model_name} has been saved to {model_dir}.")
    except Exception as e:
        print(f"An error occurred while downloading {model_name}: {e}")

print("Model downloads complete.")
