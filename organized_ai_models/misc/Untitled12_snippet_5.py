from transformers import AutoModelForCausalLM, AutoTokenizer
import shutil

# Define model name
model_name = "gpt2"

# Download and save GPT-2
print(f"Downloading {model_name} model and tokenizer...")
gpt2_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./gpt2_model")
gpt2_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./gpt2_model")
print(f"{model_name} download complete.")

# Move to Google Drive
drive_path = "/content/drive/My Drive/ModelStorage/gpt2_model"
shutil.move("./gpt2_model", drive_path)
print(f"{model_name} saved to Google Drive at {drive_path}.")
