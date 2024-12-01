from transformers import AutoModelForCausalLM, AutoTokenizer

# Define model name
model_name = "EleutherAI/gpt-j-6B"

# Download GPT-J-6B Model and Tokenizer
print("Downloading GPT-J-6B model and tokenizer...")
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./gpt_j_6b_model")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./gpt_j_6b_model")
print("GPT-J-6B download complete.")
