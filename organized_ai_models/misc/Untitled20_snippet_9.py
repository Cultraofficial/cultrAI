from transformers import AutoModel, AutoTokenizer
from huggingface_hub import hf_hub_download

# Hugging Face authentication
token = "your_huggingface_token"

# Cleaned list of model identifiers
model_ids = [
    "cardiffnlp/twitter-roberta-base-sentiment",
    "EleutherAI/gpt-neo-1.3B",
    "facebook/bart-large-cnn",
    "Salesforce/codegen-350M-mono",
    "google/mt5-small",
    "openai/whisper-base",
    "facebook/bart-large",
    "allenai/longformer-base-4096",
    "sentence-transformers/all-mpnet-base-v2",
    "huggingface/CodeBERTa-small-v1",
    "stabilityai/stablelm-base-alpha-7b",
    "google/t5-3b",
    "facebook/opt-13b",
]

# Retry downloads
for model_id in model_ids:
    try:
        print(f"🔄 Downloading model: {model_id}")
        model = AutoModel.from_pretrained(model_id, use_auth_token=token)
        tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=token)
        print(f"✅ Successfully downloaded: {model_id}")
    except Exception as e:
        print(f"❌ Failed to download {model_id}: {str(e)}")
