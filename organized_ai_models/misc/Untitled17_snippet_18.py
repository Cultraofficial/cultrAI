from google.colab import drive
import os

# Mount Google Drive to access the files
drive.mount("/content/drive", force_remount=True)

# Directories to check in Google Drive
directories_to_check = [
    "/content/drive/My Drive/Colab_models",
    "/content/drive/My Drive/colab_models"
]

# List to store all files from both directories
combined_files = []

# Loop through both directories and add their contents
for directory in directories_to_check:
    if os.path.exists(directory):
        combined_files.extend(os.listdir(directory))
    else:
        print(f"Directory not found: {directory}")

# Remove any potential duplicate file names from the list
combined_files = list(set(combined_files))

# List of models already downloaded (from your previous list)
already_downloaded_models = [
    "EleutherAI_gpt-neox-3B-finetuned", "microsoft_codex-cushman", "HuggingFace_transformerXL-large",
    "google_t5-3b", "openai_dall-e-mini", "facebook_opt-13b-finetuned", "facebook_fairseq-transformer",
    "google_t5-11b", "EleutherAI_gpt-j-8B-finetuned", "distilgpt2", "distilroberta-base", "cardiffnlp",
    "EleutherAI", "deepset", "microsoft", "allenai", "sentence-transformers", "facebook", "Salesforce",
    "openai", "bigscience", "cardiffnlp_twitter-roberta-base-sentiment", "EleutherAI_gpt-neo-125M",
    "deepset_roberta-base-squad2", "download_log.txt", "microsoft_codebert-base-mlm", "allenai_longformer-base-4096",
    "sentence-transformers_all-MiniLM-L6-v2", "facebook_bart-large-cnn", "EleutherAI_gpt-neo-1.3B", "facebook_opt-1.3b",
    "EleutherAI_gpt-neo-2.7B", "facebook_bart-large-xsum", "facebook_opt-2.7b", "Salesforce_codegen-350M-mono",
    "microsoft_DialoGPT-medium", "facebook_bart-large-mnli", "openai_whisper-base", "bigscience_bloom-560m",
    "facebook_opt-6.7b", "EleutherAI_gpt-j-6B", "bigscience_T0_3B", "cardiffnlp_twitter-roberta-base-sentiment",
    "EleutherAI_gpt-neo-125M", "deepset_roberta-base-squad2", "huggingface_CodeBERTa-small-v1", "facebook_bart-large-xsum",
    "google_t5-large", "t5-large", "facebook_mbart-large-50", "EleutherAI_gpt-j-6B", "microsoft_DialoGPT-large",
    "deepset_roberta-large-squad2", "stabilityai_stablelm-base-alpha-7b", "EleutherAI_gpt-neo-125m",
    "openai_whisper-tiny", "facebook_m2m100-418M", "Salesforce_codegen-2B", "facebook_opt-2.7b", "bigscience_bloom-560m",
    "google_t5-base", "google_mt5-xxl", "microsoft_codebert-base-mlm", "models--bigscience--T0_3B", ".locks",
    "models--facebook--opt-13b", "models--bigscience--bloom-7b1", "EleutherAI_gpt-neo-4.6B", "openai_whisper-large",
    "bigscience_T0pp", "facebook_opt-30b", "EleutherAI_gpt-neo-2.7B-finetuned", "google_t5-11b", "EleutherAI_gpt-j-8B-large",
    "google_t5-xlm-100b", "microsoft_codegen-13b", "bigscience_bloom-176b", "facebook_opt-66b", "bigscience_T0_3B",
    "facebook_opt-6.7b", "EleutherAI_gpt-neox-20B", "facebook_opt-13b", "bigscience_bloom-7b1", "google_t5-small",
    "EleutherAI_gpt-neox-3B-finetuned", "openai_whisper-small", "microsoft_codex-cushman", "HuggingFace_transformerXL-large",
    "google_t5-3b", "openai_dall-e-mini", "facebook_opt-13b-finetuned", "facebook_fairseq-transformer", "bigscience_bloom-3b",
    "EleutherAI_gpt-j-8B-finetuned"
]

# Check for duplicates
duplicate_models = [model for model in already_downloaded_models if model.replace("/", "_") in combined_files]

# List the models that are already downloaded
print(f"Found the following models already downloaded:\n{duplicate_models}\n")

# New list to download (excluding already downloaded models)
models_to_download = [model for model in already_downloaded_models if model.replace("/", "_") not in combined_files]

# Show remaining models to download
print(f"\nRemaining models to download:\n{models_to_download}")
