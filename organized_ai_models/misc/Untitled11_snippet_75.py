from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Define the model name
model_name = "google/t5-xxl"

# Download the model and tokenizer
print("Downloading T5-XXL model and tokenizer...")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir="./t5_xxl_model")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./t5_xxl_model")
print("Download complete.")
