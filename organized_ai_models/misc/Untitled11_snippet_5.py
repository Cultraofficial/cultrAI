from transformers import AutoModelForCausalLM, AutoTokenizer

# Define model name
gpt_neox_model_name = "EleutherAI/gpt-neox-20b"

# Download GPT-NeoX-20B Model and Tokenizer
print("Downloading GPT-NeoX-20B model and tokenizer...")
gpt_neox_model = AutoModelForCausalLM.from_pretrained(gpt_neox_model_name, cache_dir="./gpt_neox_20b_model")
gpt_neox_tokenizer = AutoTokenizer.from_pretrained(gpt_neox_model_name, cache_dir="./gpt_neox_20b_model")
print("GPT-NeoX-20B download complete.")
