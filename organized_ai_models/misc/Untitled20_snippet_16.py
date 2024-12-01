from huggingface_hub import hf_hub_download
from transformers import AutoModel, AutoTokenizer
import os
import gc
import psutil

# Authenticate with Hugging Face tokens
os.environ["HF_TOKEN"] = "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"  # Token 1
os.environ["HF_AUTH_TOKEN"] = "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"  # Token 2

# Set save path for models in Google Drive
save_path = "/content/drive/My Drive/downloaded_models"
os.makedirs(save_path, exist_ok=True)

# Log file for tracking downloads
log_file = os.path.join(save_path, "download_log.txt")

# Function to log successful downloads
def log_download(repo_id):
    with open(log_file, "a") as log:
        log.write(f"{repo_id}\n")

# Function to check if a model is already downloaded
def is_downloaded(repo_id):
    if os.path.exists(log_file):
        with open(log_file, "r") as log:
            downloaded_models = log.read().splitlines()
        return repo_id in downloaded_models
    return False

# Clear RAM and disk cache
def clear_ram_and_disk():
    gc.collect()
    os.system("sync && echo 3 > /proc/sys/vm/drop_caches")
    print(f"✅ RAM and disk cache cleared! Current usage: {psutil.virtual_memory().percent}% RAM.")

# List of 100 prioritized models
models = [
    # Mirror Effect AI
    "deepmind/ai-mirror-multimodel-fusion",

    # cultrAI Training Models
    "EleutherAI/gpt-neox-20b",
    "stabilityai/stablelm-base-alpha-7b",
    "meta-llama/Llama-2-13b",

    # Twin AI
    "openai/whisper-large",

    # Groundbreaking Cutting-Edge AI Models
    "bigscience/bloom",
    "EleutherAI/gpt-j-6B",
    "google/flan-t5-xxl",
    "mistralai/Mistral-7B",
    "facebook/opt-66b",
    "stabilityai/stablelm-tuned-alpha-7b",
    "facebook/galactica-30b",
    "google/mt5-large",
    "allenai/longformer-large-4096",
    "microsoft/deberta-v3-large",
    "bigscience/bigscience-p3",
    "google/t5-3b",
    "cohere-ai/cohere-xlarge",
    "huggingface/CodeBERTa-small-v1",
    "Salesforce/codegen-2B-multi",
    "openai/gpt-4-beta",
    "ai21/j1-jumbo",
    "nvidia/megatron-bert-345m",
    "anthropic/claude-v1",
    "facebook/blenderbot-3b",
    "EleutherAI/gpt-neo-2.7B",
    "sentence-transformers/all-mpnet-base-v2",
    "ai21/j1-large",
    "openai/davinci",
    "google/pegasus-large",
    "facebook/bart-large-cnn",
    "google/tapas-large",
    "openai/clip-vit-large",
    "allenai/macaw-large",
    "Salesforce/blip2-vision-language",
    "facebook/detr-resnet-50",
    "deepmind/alphafold2",
    "mistralai/Mistral-13B",
    "Salesforce/codegen-350M-mono",
    "stabilityai/stable-diffusion-v1-5",
    "facebook/fairseq-wav2vec2-large",
    "microsoft/speecht5-large",
    "openai/whisper-base",
    "EleutherAI/pythia-12B",
    "google/flan-ul2",
    "Salesforce/codexglue",
    "meta-llama/llama-65b",
    "EleutherAI/pythia-6.9B",
    "microsoft/codebert",
    "stabilityai/sdxl-base-1.0",
    "bigscience/bloom-7b1",
    "EleutherAI/pythia-2.8B",
    "huggingface/diffusers",
    "openai/codex-cushman-001",
    "facebook/blenderbot-90M",
    "stabilityai/instruct-pix2pix",
    "google/long-t5-tglobal-xl",
    "google/byt5-large",
    "facebook/fastspeech2-en",
    "deepmind/alphacode",
    "openai/gpt-4-turbo",
    "google/t5-v1_1-large",
    "ai21/j1-grande",
    "facebook/m2m-100-1.2B",
    "deepmind/perceiver-io",
    "huggingface/transformers",
    "facebook/faster-rcnn-resnet50",
    "facebook/deepmask",
    "facebook/bart-base",
    "microsoft/deberta-xlarge-v2",
    "openai/ada",
    "Salesforce/blip-2-xl",
    "meta-segmenter-xl",
    "Salesforce/blip-2-coco",
    "deepmind/gopher",
    "Salesforce/palm",
    "google/ul2-20b",
    "ai21/j2-ultra",
    "openai/text-davinci-002",
    "stabilityai/imagen",
    "EleutherAI/gpt-j-1B",
    "openai/codex-davinci-002",
    "facebook/detectron2",
    "huggingface/hubert-large-ls960",
    "stabilityai/clip-vision-transformer",
    "stabilityai/imagenet-pretrained-vit",
    "Salesforce/unifiedqa-large",
    "microsoft/speecht5-base",
    "deepmind/wavenet",
    "facebook/maskrcnn-resnet50",
    "Salesforce/pangu",
    "google/pegasus-large-tf",
    "EleutherAI/pythia-20B",
    "huggingface/tokenizers",
    "facebook/mixup-resnet50",
]

# Function to download and save models
def download_and_save_model(repo_id, save_path):
    if is_downloaded(repo_id):
        print(f"✅ Skipping already downloaded: {repo_id}")
        return

    try:
        model_path = os.path.join(save_path, repo_id.replace("/", "_"))
        os.makedirs(model_path, exist_ok=True)
        AutoModel.from_pretrained(repo_id, cache_dir=model_path, use_auth_token=True)
        AutoTokenizer.from_pretrained(repo_id, cache_dir=model_path, use_auth_token=True)
        print(f"✅ Successfully downloaded and saved: {repo_id}")
        log_download(repo_id)  # Log success
        clear_ram_and_disk()  # Clear RAM and disk after download
    except Exception as e:
        print(f"❌ Failed to download {repo_id}: {str(e)}")

# Download all models
for model in models:
    download_and_save_model(model, save_path)
