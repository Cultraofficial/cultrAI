from transformers import AutoModelForCausalLM, AutoModelForMaskedLM, AutoTokenizer
import shutil

# Define Google Drive path
drive_path = "/content/drive/My Drive/ModelStorage"

# Download and save distilgpt2_model
model_name = "distilgpt2"
print(f"Downloading {model_name} model and tokenizer...")
distilgpt2_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=f"./{model_name}")
distilgpt2_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=f"./{model_name}")
print(f"{model_name} download complete.")
shutil.move(f"./{model_name}", f"{drive_path}/{model_name}_model")
print(f"{model_name} saved to Google Drive.\n")

# Download and save bert_base_model
model_name = "bert-base-uncased"
print(f"Downloading {model_name} model and tokenizer...")
bert_base_model = AutoModelForMaskedLM.from_pretrained(model_name, cache_dir=f"./{model_name}")
bert_base_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=f"./{model_name}")
print(f"{model_name} download complete.")
shutil.move(f"./{model_name}", f"{drive_path}/bert_base_model")
print(f"{model_name} saved to Google Drive.\n")

# Download and save dalle_mini_model
model_name = "dalle-mini/dalle-mini"
print(f"Downloading {model_name} model and tokenizer...")
dalle_mini_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=f"./dalle_mini_model")
dalle_mini_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=f"./dalle_mini_model")
print(f"{model_name} download complete.")
shutil.move(f"./dalle_mini_model", f"{drive_path}/dalle_mini_model")
print(f"{model_name} saved to Google Drive.\n")
