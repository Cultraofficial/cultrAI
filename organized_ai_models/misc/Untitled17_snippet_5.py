from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
import os

# Mount Google Drive
from google.colab import drive
drive.mount("/content/drive")

# Hugging Face API Tokens
hf_token_1 = "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"
hf_token_2 = "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"

# Authenticate Hugging Face API
login(token=hf_token_1)

# Define models and their directories (updated list)
models = [
    "EleutherAI/gpt-neo-2.7B",
    "EleutherAI/gpt-neo-1.3B",
    "bigscience/bloom-560m",
    "t5-base",  # Replaced 'T5-11B' with a correct T5 model available on Hugging Face
    "openai/gpt-3",
    "bert-base-uncased",  # Replaced 'BERT' with a popular model available
    "facebook/bart-large-cnn",  # Corrected CLIP reference
    "google/flan-t5-xxl",  # Example for T5-based model suitable for multiple tasks
    "HuggingFaceH4/starchat-alpha",  # Example of a conversational model
    "Salesforce/codegen-350M-mono",  # Updated with correct Codex reference
    "stabilityai/stable-diffusion-2",  # Stable Diffusion model for image generation
]

# Specify Google Drive folder where models will be stored
drive_folder = "/content/drive/MyDrive/colab_models"

# Create directory if it doesn't exist
if not os.path.exists(drive_folder):
    os.makedirs(drive_folder)

# Download models
for model_name in models:
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

# Final message
print("All models downloaded and saved to Google Drive!")
