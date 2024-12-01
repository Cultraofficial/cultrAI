from transformers import AutoModelForCausalLM, AutoTokenizer

# Define model name
llama_7b_model_name = "huggingface/llama-7b"

# Download LLaMA-7B Model and Tokenizer
print("Downloading LLaMA-7B model and tokenizer...")
llama_7b_model = AutoModelForCausalLM.from_pretrained(llama_7b_model_name, cache_dir="./llama_7b_model")
llama_7b_tokenizer = AutoTokenizer.from_pretrained(llama_7b_model_name, cache_dir="./llama_7b_model")
print("LLaMA-7B download complete.")
