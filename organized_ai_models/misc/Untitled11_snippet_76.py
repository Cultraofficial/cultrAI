from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Define the model name
model_name = "t5-large"

# Download the model and tokenizer
print("Downloading T5-Large model and tokenizer...")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir="./t5_large_model")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./t5_large_model")
print("Download complete.")