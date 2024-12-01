from transformers import AutoModel, AutoTokenizer

# List of models to download
models = [
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
    "facebook/opt-13b",
]

# Function to download and save models
def download_and_save_model(model_name, save_directory):
    try:
        print(f"🔄 Downloading model: {model_name}")
        model = AutoModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Save the model and tokenizer
        model.save_pretrained(os.path.join(save_directory, model_name.replace("/", "_")))
        tokenizer.save_pretrained(os.path.join(save_directory, model_name.replace("/", "_")))

        print(f"✅ Successfully downloaded and saved: {model_name}")
    except Exception as e:
        print(f"❌ Failed to download {model_name}: {e}")

# Download all models
for model in models:
    download_and_save_model(model, save_directory)
