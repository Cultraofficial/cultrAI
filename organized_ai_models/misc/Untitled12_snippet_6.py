import os

# Path to the ModelStorage directory in Google Drive
drive_path = "/content/drive/My Drive/ModelStorage"

# Check and list all models in the directory
print("Checking models already uploaded to Google Drive:")
if os.path.exists(drive_path):
    uploaded_models = os.listdir(drive_path)
    print("Models already uploaded:")
    for model in uploaded_models:
        print(f"- {model}")
else:
    print("ModelStorage directory not found in Google Drive.")

print("\nModels remaining to be uploaded:")
# List of models expected to be downloaded and saved
expected_models = [
    "bart_large_model", "bert_base_model", "bloom_model", "clip_model",
    "codebert_model", "dalle_mini_model", "distilbert_multilingual_model",
    "gpt2_large_model", "gpt2_medium_model", "gpt2_model", "gpt_j_6b_model",
    "gpt_neox_20b_model", "stable_diffusion_model", "t5_large_model",
    "whisper_tiny_model", "distilgpt2_model", "gpt_neo_125M_model"
]

# Identify models not yet uploaded
remaining_models = [model for model in expected_models if model not in uploaded_models]
for model in remaining_models:
    print(f"- {model}")
