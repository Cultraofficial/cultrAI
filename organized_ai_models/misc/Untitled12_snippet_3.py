from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# Define model name and Google Drive path for model storage
model_name = "distilgpt2"
save_dir = "/content/drive/My Drive/ModelStorage/distilgpt2"
os.makedirs(save_dir, exist_ok=True)

# Download and save DistilGPT-2
print(f"Downloading {model_name} model and tokenizer...")
distilgpt2_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./distilgpt2")
distilgpt2_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./distilgpt2")

# Save model and tokenizer to Google Drive
torch.save(distilgpt2_model.state_dict(), f"{save_dir}/model.pth")
distilgpt2_tokenizer.save_pretrained(save_dir)
print(f"{model_name} saved to Google Drive.")
