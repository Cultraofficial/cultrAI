from transformers import AutoModelForMaskedLM, AutoTokenizer

# Define the model name
model_name = "bert-base-uncased"

# Download the model and tokenizer
print("Downloading BERT-base-uncased model and tokenizer...")
model = AutoModelForMaskedLM.from_pretrained(model_name, cache_dir="./bert_base_model")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./bert_base_model")
print("Download complete.")
