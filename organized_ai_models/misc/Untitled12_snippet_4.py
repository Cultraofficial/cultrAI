from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# Define model name and Google Drive path for model storage
model_name = "EleutherAI/gpt-neo-125M"
save_dir = "/content/drive/My Drive/ModelStorage/gpt_neo_125m"
os.makedirs(save_dir, exist_ok=True)

# Download and save GPT-Neo-125M
print(f"Downloading {model_name} model and tokenizer...")
gpt_neo_125m_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./gpt_neo_125m")
gpt_neo_125m_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./gpt_neo_125m")

# Save model and tokenizer to Google Drive
torch.save(gpt_neo_125m_model.state_dict(), f"{save_dir}/model.pth")
gpt_neo_125m_tokenizer.save_pretrained(save_dir)
print(f"{model_name} saved to Google Drive.")
