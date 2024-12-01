from transformers import AutoModelForCausalLM, AutoTokenizer

# Define model name
model_name = "gpt2-large"

# Download GPT-2 Large Model and Tokenizer
print("Downloading GPT-2 Large model and tokenizer...")
gpt2_large_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./gpt2_large_model")
gpt2_large_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./gpt2_large_model")
print("GPT-2 Large download complete.")
