from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# Define both tokens
tokens = [
    "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",
    "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"
]

# Try each token until successful login
authenticated = False
for token in tokens:
    try:
        login(token=token)
        print("Authenticated successfully with token.")
        authenticated = True
        break
    except Exception as e:
        print(f"Token failed: {e}")

if not authenticated:
    raise ValueError("All tokens failed. Check your Hugging Face tokens.")

# List of models to download
model_names = [
    "togethercomputer/OpenChatKit",
    "EleutherAI/gpt-neox-20b",
    "mistralai/Mistral",
    # Add any other models you want here
]

# Attempt to download each model
for model_name in model_names:
    try:
        print(f"Attempting to download {model_name}...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        print(f"{model_name} downloaded successfully.")
    except Exception as e:
        print(f"Failed to download {model_name}: {e}")
