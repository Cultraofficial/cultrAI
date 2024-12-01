import os
import gc
from huggingface_hub import HfApi
from transformers import AutoModel, AutoTokenizer
import torch

# Set up Hugging Face token (replace with your token if needed)
token = "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"

# Target directory for downloaded models
target_dir = "/content/drive/My Drive/Colab_models"
os.makedirs(target_dir, exist_ok=True)

# Models to download
models_to_download = [
    "stabilityai/stablelm-base-alpha-7b",
    "EleutherAI/pythia-12b",
    "facebook/opt-66b",
    "EleutherAI/gpt-j-6B",
]

# Function to clear RAM
def clear_memory():
    torch.cuda.empty_cache()
    gc.collect()

# Download and load each model sequentially
api = HfApi()
for model_name in models_to_download:
    print(f"\nAttempting to download {model_name}...")

    model_dir = os.path.join(target_dir, model_name.split("/")[-1])
    if os.path.exists(model_dir):
        print(f"{model_name} is already downloaded, skipping.")
        continue

    # Download model and tokenizer
    try:
        model = AutoModel.from_pretrained(model_name, cache_dir=target_dir, use_auth_token=token)
        tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=target_dir, use_auth_token=token)
        print(f"Successfully downloaded and saved {model_name}.")
    except Exception as e:
        print(f"Failed to download {model_name}: {e}")
        continue

    # Save model to specified directory
    model.save_pretrained(model_dir)
    tokenizer.save_pretrained(model_dir)

    # Clear memory after each model
    del model, tokenizer
    clear_memory()
    print(f"Memory cleared after saving {model_name}.")

print("All downloads complete.")
