from google.colab import drive
from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import time

# Mount Google Drive
drive.mount("/content/drive")

# Hugging Face API Tokens (Automatically applied)
hf_token_1 = "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"
hf_token_2 = "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"

# Authenticate Hugging Face API
login(token=hf_token_1)

# List of models to download
models = [
    "EleutherAI/gpt-neox-20B",
    "EleutherAI/gpt-neo-2.7B",
    "EleutherAI/gpt-neo-1.3B",
    "Meta AI LaMDA",
    "BigScience/bloom-560m",
    "T5-11B",
    "Codex Cushman",
    "Codex Davinci-2",
    "CLIP",
    "Blip-2",
    "LAVIS",
    "Perceiver IO",
    "DialogPT",
    "Replika AI",
    "MoralBERT",
    "Fairseq",
    "Social-CausalBERT",
    "SpeculativeGPT",
    "TransferNet",
    "Whisper Large",
    "Whisper Medium",
    "DALL-E 3",
    "Vision Transformer (ViT)",
    "DeepLab",
    "MetaRL",
    "Galois",
    "DeepMind MuZero",
    "CurriculumNet",
    "Knowledge Graph AI (Aristo)",
    "GPT-J",
    "BigGAN",
    "Stable Diffusion",
    "Gato",
    "GazeGAN",
    "Reinforcement AI"
]

# Specify Google Drive folder where models will be stored
drive_folder = "/content/drive/MyDrive/colab_models"

# Create directory if it doesn't exist
if not os.path.exists(drive_folder):
    os.makedirs(drive_folder)

# Function to download and save models with retry logic
def download_model_with_retry(model_name, retries=3):
    try:
        print(f"Downloading {model_name}...")
        model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=hf_token_1)
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token_1)

        # Save to Google Drive
        model.save_pretrained(f"{drive_folder}/{model_name}")
        tokenizer.save_pretrained(f"{drive_folder}/{model_name}")
        print(f"{model_name} downloaded and saved successfully!")
    except Exception as e:
        print(f"Failed to download {model_name}. Error: {e}")
        if retries > 0:
            print(f"Retrying {model_name}...")
            time.sleep(30)  # Wait before retry
            download_model_with_retry(model_name, retries - 1)
        else:
            print(f"Failed to download {model_name} after multiple retries.")

# Download all models with retries
for model_name in models:
    download_model_with_retry(model_name)

# Final message
print("All models downloaded and saved to Google Drive!")
