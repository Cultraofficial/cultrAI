from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoModelForSeq2SeqLM

# Define model names
distilbert_multilingual_model_name = "distilbert-base-multilingual-cased"
bart_large_model_name = "facebook/bart-large"

# Download DistilBERT Multilingual Model and Tokenizer
print("Downloading DistilBERT Multilingual model and tokenizer...")
distilbert_multilingual_model = AutoModelForSequenceClassification.from_pretrained(distilbert_multilingual_model_name, cache_dir="./distilbert_multilingual_model")
distilbert_multilingual_tokenizer = AutoTokenizer.from_pretrained(distilbert_multilingual_model_name, cache_dir="./distilbert_multilingual_model")
print("DistilBERT Multilingual download complete.")

# Download BART Large Model and Tokenizer
print("Downloading BART Large model and tokenizer...")
bart_large_model = AutoModelForSeq2SeqLM.from_pretrained(bart_large_model_name, cache_dir="./bart_large_model")
bart_large_tokenizer = AutoTokenizer.from_pretrained(bart_large_model_name, cache_dir="./bart_large_model")
print("BART Large download complete.")
