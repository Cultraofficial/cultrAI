from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "facebook/opt-2.7b"  # Replace this if a different model is next on your list
print(f"Downloading {model_name} model and tokenizer...")

# Download and save the model and tokenizer
opt_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./opt_2.7b")
opt_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./opt_2.7b")
print(f"{model_name} download complete.")

# Save to Google Drive
!mv ./opt_2.7b /content/drive/My\ Drive/ModelStorage/opt_2.7b_model
print(f"{model_name} saved to Google Drive at /content/drive/My Drive/ModelStorage/opt_2.7b_model.")
