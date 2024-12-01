from transformers import AutoModelForSeq2SeqLM, AutoModelForCausalLM, AutoModelForMaskedLM, AutoModel, AutoTokenizer
import shutil
import os

# Google Drive path to save models
drive_base_path = "/content/drive/My Drive/ModelStorage"

# Define smaller models for downloading
models = {
    "openai/clip-vit-base-patch32": "clip_model",
    "microsoft/codebert-base": "codebert_model",
    "distilbert-base-multilingual-cased": "distilbert_multilingual_model",
    "gpt2-medium": "gpt2_medium_model",
    "EleutherAI/gpt-j-6B": "gpt_j_6b_model",
    "t5-large": "t5_large_model",
    "openai/whisper-tiny": "whisper_tiny_model"
}

# Download and save each model to Google Drive
for model_name, model_dir in models.items():
    print(f"Downloading {model_name}...")

    # Determine the appropriate model class to use
    if "seq2seq" in model_name.lower() or "bart" in model_name.lower() or "t5" in model_name.lower():
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=f"./{model_dir}")
    elif "causal" in model_name.lower() or "gpt" in model_name.lower():
        model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=f"./{model_dir}")
    elif "masked" in model_name.lower() or "bert" in model_name.lower() or "codebert" in model_name.lower():
        model = AutoModelForMaskedLM.from_pretrained(model_name, cache_dir=f"./{model_dir}")
    else:
        model = AutoModel.from_pretrained(model_name, cache_dir=f"./{model_dir}")

    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=f"./{model_dir}")
    print(f"{model_name} download complete.")

    # Move model to Google Drive
    drive_path = os.path.join(drive_base_path, model_dir)
    os.makedirs(drive_path, exist_ok=True)
    shutil.move(f"./{model_dir}", drive_path)
    print(f"{model_name} saved to Google Drive at {drive_path}.")

print("Selected models have been downloaded and saved to Google Drive.")
