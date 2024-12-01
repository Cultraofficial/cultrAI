from transformers import AutoModelForCausalLM, AutoTokenizer

# Define the model name
model_name = "gpt2"

# Download the model and tokenizer
print("Downloading GPT-2 model and tokenizer...")
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./gpt2_model")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./gpt2_model")
print("Download complete.")
