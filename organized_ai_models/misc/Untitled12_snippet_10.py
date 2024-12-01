from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "facebook/opt-6.7b"  # Replace with the next larger model if different
print(f"Downloading {model_name} model and tokenizer...")

# Download and save the model and tokenizer
opt_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./opt_6.7b")
opt_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./opt_6.7b")
print(f"{model_name} download complete.")

# Save to Google Drive
!mv ./opt_6.7b /content/drive/My\ Drive/ModelStorage/opt_6.7b_model
print(f"{model_name} saved to Google Drive at /content/drive/My Drive/ModelStorage/opt_6.7b_model.")
