# Adjust Google Drive save path to ensure consistency
save_path = "/content/drive/My Drive/Colab_models/"

# Remaining models to download, skipping those with access issues
next_models_to_download = [
    "EleutherAI/gpt-neo-4.6B",
    "bigscience/bloom-560m",
    "stabilityai/stablelm-base-alpha-7b",
    # Add additional models from your list here
]

# Function to download and save model to the correct folder
def download_and_save_model(model_name, token=os.getenv("HUGGING_FACE_TOKEN")):
    print(f"Starting download for model: {model_name}")
    try:
        model = AutoModel.from_pretrained(model_name, use_auth_token=token)
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)

        # Save to specified path
        model.save_pretrained(f"{save_path}{model_name}")
        tokenizer.save_pretrained(f"{save_path}{model_name}")

        print(f"Downloaded and saved: {model_name}")
        del model, tokenizer
        torch.cuda.empty_cache()  # Clear GPU cache if available

    except Exception as e:
        print(f"Failed to download {model_name}. Error: {e}")

# Download the next set of models
for model_name in next_models_to_download:
    download_and_save_model(model_name)
