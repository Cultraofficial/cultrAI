from transformers import AutoModelForCausalLM, AutoTokenizer

# Define the model name
model_name = "EleutherAI/gpt-neo-1.3B"

# Download the model and tokenizer
print("Downloading GPT-Neo 1.3B model and tokenizer...")
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./gpt_neo_1.3B_model")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./gpt_neo_1.3B_model")
print("Download complete.")
