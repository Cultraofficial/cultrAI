from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Define the model name
model_name = "distilbert-base-uncased"

# Download the model and tokenizer
print("Downloading DistilBERT model and tokenizer...")
model = AutoModelForSequenceClassification.from_pretrained(model_name, cache_dir="./distilbert_model")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./distilbert_model")
print("Download complete.")