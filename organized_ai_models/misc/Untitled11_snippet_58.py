from transformers import AutoModelForCausalLM, AutoTokenizer

# Specify model name on Hugging Face
model_name = "bigscience/bloom"

# Download model and tokenizer
print("Downloading BLOOM model and tokenizer...")
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./bloom_model")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./bloom_model")
print("Download complete.")
