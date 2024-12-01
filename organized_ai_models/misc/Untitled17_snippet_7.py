from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSeq2SeqLM
from huggingface_hub import login
import os
import torch
from google.colab import drive

# Mount Google Drive immediately
drive.mount("/content/drive")

# Hugging Face API Tokens
hf_token_1 = "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"
hf_token_2 = "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"

# Authenticate Hugging Face API with both tokens
login(token=hf_token_1)

# Define models and their directories (updated list)
models = [
    "EleutherAI/gpt-neo-2.7B",
    "EleutherAI/gpt-neo-1.3B",
    "bigscience/bloom-560m",
    "facebook/bart-large-cnn",
    "google/flan-t5-xxl",  # Using a T5 model, handled by AutoModelForSeq2SeqLM
    "bert-base-uncased",  # BERT model for text understanding
    "HuggingFaceH4/starchat-alpha",  # Conversational model
    "Salesforce/codegen-350M-mono",  # Codegen for backend generation
    "stabilityai/stable-diffusion-2",  # Stable Diffusion for image generation
    "HuggingFaceH4/starchat-alpha",  # Conversational AI
    "EleutherAI/gpt-j",  # Another GPT model
]

# Specify Google Drive folder where models will be stored
drive_folder = "/content/drive/MyDrive/colab_models"

# Create directory if it doesn't exist
if not os.path.exists(drive_folder):
    os.makedirs(drive_folder)

# Clear disk and RAM
torch.cuda.empty_cache()

# Download models
for model_name in models:
    try:
        print(f"Downloading {model_name}...")

        # Check model type for T5 model (Seq2SeqLM)
        if "t5" in model_name.lower():
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name, use_auth_token=hf_token_1)
        else:
            model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=hf_token_1)

        tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token_1)

        # Save to Google Drive (corrected path)
        model.save_pretrained(f"{drive_folder}/{model_name}")
        tokenizer.save_pretrained(f"{drive_folder}/{model_name}")
        print(f"{model_name} downloaded and saved successfully!")
    except Exception as e:
        print(f"Failed to download {model_name}. Error: {e}")

# Final message
print("All models downloaded and saved to Google Drive!")
