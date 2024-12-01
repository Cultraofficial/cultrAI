from transformers import AutoModelForCausalLM, AutoModelForMaskedLM, AutoTokenizer

# Define model names
gpt2_xl_model_name = "gpt2-xl"
bert_large_model_name = "bert-large-uncased"

# Download GPT-2 XL Model and Tokenizer
print("Downloading GPT-2 XL model and tokenizer...")
gpt2_xl_model = AutoModelForCausalLM.from_pretrained(gpt2_xl_model_name, cache_dir="./gpt2_xl_model")
gpt2_xl_tokenizer = AutoTokenizer.from_pretrained(gpt2_xl_model_name, cache_dir="./gpt2_xl_model")
print("GPT-2 XL download complete.")

# Download BERT Large Model and Tokenizer
print("Downloading BERT Large model and tokenizer...")
bert_large_model = AutoModelForMaskedLM.from_pretrained(bert_large_model_name, cache_dir="./bert_large_model")
bert_large_tokenizer = AutoTokenizer.from_pretrained(bert_large_model_name, cache_dir="./bert_large_model")
print("BERT Large download complete.")
