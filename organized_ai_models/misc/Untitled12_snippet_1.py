from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# Define Google Drive path for model storage
save_dir = "/content/drive/My Drive/ModelStorage/gpt_neox_20b"
os.makedirs(save_dir, exist_ok=True)

# Download and save GPT-NeoX (20B)
print("Downloading GPT-NeoX (20B) model and tokenizer...")
gpt_neox_model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neox-20b", cache_dir="./gpt_neox_20b")
gpt_neox_tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b", cache_dir="./gpt_neox_20b")

# Save model and tokenizer to Google Drive
torch.save(gpt_neox_model.state_dict(), f"{save_dir}/model.pth")
gpt_neox_tokenizer.save_pretrained(save_dir)
print("GPT-NeoX (20B) saved to Google Drive.")
