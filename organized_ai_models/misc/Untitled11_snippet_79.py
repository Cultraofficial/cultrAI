from transformers import AutoModel, AutoTokenizer

# Define model names
clip_model_name = "openai/clip-vit-base-patch32"
codebert_model_name = "microsoft/codebert-base"

# Download CLIP Model and Tokenizer
print("Downloading CLIP model (ViT-B/32) and tokenizer...")
clip_model = AutoModel.from_pretrained(clip_model_name, cache_dir="./clip_model")
clip_tokenizer = AutoTokenizer.from_pretrained(clip_model_name, cache_dir="./clip_model")
print("CLIP (ViT-B/32) download complete.")

# Download CodeBERT Model and Tokenizer
print("Downloading CodeBERT model and tokenizer...")
codebert_model = AutoModel.from_pretrained(codebert_model_name, cache_dir="./codebert_model")
codebert_tokenizer = AutoTokenizer.from_pretrained(codebert_model_name, cache_dir="./codebert_model")
print("CodeBERT download complete.")
