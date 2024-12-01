from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "EleutherAI/gpt-neo-2.7B"  # Replace with the larger model name if different
print(f"Downloading {model_name} model and tokenizer...")

# Download and save the model and tokenizer
gpt_neo_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./gpt_neo_2.7B")
gpt_neo_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./gpt_neo_2.7B")
print(f"{model_name} download complete.")

# Save to Google Drive
!mv ./gpt_neo_2.7B /content/drive/My\ Drive/ModelStorage/gpt_neo_2.7B_model
print(f"{model_name} saved to Google Drive at /content/drive/My Drive/ModelStorage/gpt_neo_2.7B_model.")
