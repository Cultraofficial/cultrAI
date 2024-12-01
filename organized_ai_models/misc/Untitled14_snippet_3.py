from huggingface_hub import hf_hub_download
import os

# Path to save models
save_dir = '/content/drive/My Drive/Colab_models'
failed_downloads = []

# List of models with previous download errors
models_to_download = [
    "EleutherAI/gpt-neox-3B-finetuned",
    "microsoft/codex-cushman",
    "HuggingFace/transformerXL-large",
    "google/t5-3b",
    "openai/dall-e-mini",
    "facebook/opt-13b-finetuned",
    "facebook/fairseq-transformer",
    "google/t5-11b",
    "EleutherAI/gpt-j-8B-finetuned"
]

# Primary and secondary tokens
primary_token = "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"
secondary_token = "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"

# Download function with fallback token
def download_model(repo_id, save_dir):
    os.makedirs(os.path.join(save_dir, repo_id.replace('/', '_')), exist_ok=True)
    for filename in ["config.json", "pytorch_model.bin", "tokenizer.json", "vocab.json", "merges.txt"]:
        try:
            hf_hub_download(
                repo_id=repo_id,
                filename=filename,
                use_auth_token=primary_token,
                local_dir=os.path.join(save_dir, repo_id.replace('/', '_'))
            )
            print(f"{filename} for {repo_id} successfully saved to {os.path.join(save_dir, repo_id.replace('/', '_'))}")
        except Exception as e:
            print(f"Primary token failed for {filename} in {repo_id}: {e}")
            # Try with the secondary token if the primary fails
            try:
                hf_hub_download(
                    repo_id=repo_id,
                    filename=filename,
                    use_auth_token=secondary_token,
                    local_dir=os.path.join(save_dir, repo_id.replace('/', '_'))
                )
                print(f"{filename} for {repo_id} successfully saved using secondary token.")
            except Exception as e:
                print(f"Failed to download {filename} for {repo_id} with both tokens: {e}")
                failed_downloads.append((repo_id, filename))

# Download each model
for model in models_to_download:
    download_model(model, save_dir)

# Print any failed downloads
if failed_downloads:
    print("\nThe following files failed to download:")
    for model, file in failed_downloads:
        print(f"{model} - {file}")
else:
    print("\nAll models downloaded successfully.")
