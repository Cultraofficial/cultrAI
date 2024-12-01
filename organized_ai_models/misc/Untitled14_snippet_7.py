from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
import torch

# Authenticate
tokens = [
    "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",
    "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"
]
authenticated = False
for token in tokens:
    try:
        login(token=token)
        authenticated = True
        print("Authenticated successfully with token.")
        break
    except Exception as e:
        print(f"Token failed: {e}")

if not authenticated:
    raise ValueError("All tokens failed. Check your Hugging Face tokens.")

# Define the model name
model_name = "EleutherAI/gpt-neox-20b"

# Load tokenizer (small file, safe to load directly)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Define model save path
model_path = f"./{model_name.replace('/', '_')}_downloaded_model"

# Download each shard separately
try:
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        cache_dir=model_path,
        torch_dtype=torch.float16,
        device_map="auto"  # Automatically allocate to available resources
    )
    print("Model downloaded and loaded successfully.")
except Exception as e:
    print(f"Failed to load model: {e}")
