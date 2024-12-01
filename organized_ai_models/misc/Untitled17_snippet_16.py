from transformers import AutoModel, AutoTokenizer
import os

# Hugging Face authentication tokens
tokens = ["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", "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"]

# List of models to download (add the models you need to download here)
model_names = [
    # Replace with the models you need to download
    "new-model-1", "new-model-2",
    # additional models go here
]

# Paths for both directories to check for existing models
base_paths = ["/content/drive/My Drive/Colab_models/", "/content/drive/My Drive/colab_models/"]

# Function to download and save models if not already present
for model_name in model_names:
    model_found = False
    for base_path in base_paths:
        save_path = os.path.join(base_path, model_name.replace("/", "_"))
        if os.path.exists(save_path):
            print(f"{model_name} already exists at {save_path}, skipping download.\n")
            model_found = True
            break
    if not model_found:
        print(f"Downloading {model_name}...")
        for token in tokens:
            try:
                model = AutoModel.from_pretrained(model_name, use_auth_token=token)
                tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)
                os.makedirs(save_path, exist_ok=True)  # Ensure directory exists
                model.save_pretrained(save_path)
                tokenizer.save_pretrained(save_path)
                print(f"Successfully downloaded and saved {model_name} at {save_path}\n")
                break  # Exit the token loop if download is successful
            except Exception as e:
                print(f"Failed to download {model_name} with token. Trying next token if available. Error: {e}")
                continue  # Try the next token
        else:
            print(f"Failed to download {model_name} with all provided tokens.")

print("Download process completed. Please verify in both Google Drive directories.")
