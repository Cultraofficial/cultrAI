import os

# Define the Google Drive model storage path
model_storage_path = "/content/drive/My Drive/ModelStorage"

# List of expected model directories in Google Drive
expected_models = [
    "bart_large_model",
    "bert_base_model",
    "bloom_model",
    "clip_model",
    "codebert_model",
    "dalle_mini_model",
    "distilbert_multilingual_model",
    "gpt2_large_model",
    "gpt2_medium_model",
    "gpt2_model",
    "gpt_j_6b_model",
    "gpt_neox_20b_model",
    "stable_diffusion_model",
    "t5_large_model",
    "whisper_tiny_model"
]

# Check if each expected model exists in the ModelStorage folder
for model_name in expected_models:
    model_path = os.path.join(model_storage_path, model_name)
    if os.path.exists(model_path):
        print(f"{model_name} exists in Google Drive.")
    else:
        print(f"Error: {model_name} is missing in Google Drive.")
