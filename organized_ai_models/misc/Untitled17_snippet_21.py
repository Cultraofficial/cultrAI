# Step 1: Hook up Google Drive with manual authentication
from google.colab import drive
drive.mount('/content/drive')

# Step 2: Import required libraries for downloading models
from transformers import AutoModel, AutoTokenizer
import os

# Set the Google Drive path to save models
drive_path = '/content/drive/My Drive/colab_models/'

# List of models to download (Only models that were accessible or had alternatives)
models_to_download = [
    'bigscience/bloom-560m',  # Already downloaded successfully
    'EleutherAI/gpt-neo-2.7B',
    'facebook/bart-large-cnn',
    'microsoft/codebert-base-mlm',
    # Add more models you know work below (models that passed or have alternatives)
]

# Step 3: Define function to download models with error handling
def download_model(model_name):
    try:
        # Download the model and tokenizer
        print(f"Downloading {model_name}...")
        model = AutoModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Save the model to Google Drive
        model.save_pretrained(drive_path + model_name)
        tokenizer.save_pretrained(drive_path + model_name)
        print(f"{model_name} downloaded and saved to Google Drive.")
    except Exception as e:
        print(f"Failed to download {model_name}. Error: {str(e)}")

# Step 4: Loop through models to download
for model in models_to_download:
    download_model(model)

# Step 5: Check for alternative models for the ones that failed
# Below you can include alternative models if needed
alternative_models = [
    'EleutherAI/gpt-neo-1.3B',  # Replace these with your preferred alternative models
    'facebook/bart-large-xsum',
    'openai/gpt-3.5-turbo',
    # Add more fallback models here
]

# Download alternatives if necessary
for model in alternative_models:
    download_model(model)

print("All accessible models have been processed.")
