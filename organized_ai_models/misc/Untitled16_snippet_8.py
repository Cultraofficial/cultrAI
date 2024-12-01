from transformers import AutoModel, AutoTokenizer

# Revised list of 25 smaller models to download, excluding duplicates
model_names = [
    "sentence-transformers/all-MiniLM-L6-v2", "cardiffnlp/twitter-roberta-base-sentiment",
    "deepset/roberta-base-squad2", "microsoft/codebert-base-mlm", "sentence-transformers/all-mpnet-base-v2",
    "facebook/bart-large-cnn", "google/t5-small", "EleutherAI/gpt-neo-125M", "facebook/opt-1.3b",
    "Salesforce/codegen-350M-mono", "allenai/longformer-base-4096", "microsoft/DialoGPT-medium",
    "facebook/bart-large-mnli", "openai/whisper-base", "bigscience/bloom-560m", "google/pegasus-cnn_dailymail",
    "huggingface/CodeBERTa-small-v1", "facebook/mbart-large-50", "facebook/m2m100-418M", "facebook_opt-2.7b",
    "openai/whisper-tiny", "facebook_m2m100-418M", "Salesforce/codegen-2B", "bigscience_bloom-3b",
    "google_t5-base"
]

# Download each model and tokenizer
for model_name in model_names:
    print(f"Downloading {model_name}...")
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print(f"Successfully downloaded {model_name}\n")
