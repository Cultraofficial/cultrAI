from transformers import AutoModelForCausalLM, AutoTokenizer

# Define model name
model_name = "gpt2-medium"

# Download GPT-2 Medium Model and Tokenizer
print("Downloading GPT-2 Medium model and tokenizer...")
gpt2_medium_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./gpt2_medium_model")
gpt2_medium_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./gpt2_medium_model")
print("GPT-2 Medium download complete.")
