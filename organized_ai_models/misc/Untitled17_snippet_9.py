# Start by mounting Google Drive
from google.colab import drive
drive.mount("/content/drive")

# List of first 50 AI models
ai_models = [
    "EleutherAI/gpt-neo-2.7B", "EleutherAI/gpt-neo-1.3B", "bigscience/bloom-560m",
    "facebook/bart-large-cnn", "google/flan-t5-xxl", "bert-base-uncased",
    "HuggingFaceH4/starchat-alpha", "openai/gpt-3", "EleutherAI/gpt-j",
    "EleutherAI/gpt-neo-x-2.7B", "facebook/bart-large-xsum", "bigscience/bloom-3B",
    "facebook/bart-large-cnn", "HuggingFaceH4/starchat-alpha", "google/flan-t5-small",
    "microsoft/DeBERTa-v3-small", "EleutherAI/gpt-j-6B", "t5-base",
    "google/bert-large-cased", "DeepMind/alfred", "EleutherAI/gpt-neo-175B",
    "microsoft/roberta-base", "google/bert-base-uncased", "t5-large",
    "microsoft/roberta-large", "EleutherAI/gpt-neo-1.3B", "facebook/blip-2",
    "huggingface/llama-7b", "stablediffusion-v1-4", "DeepMind/muzero",
    "facebook/detectron", "BERT-base-multilingual", "openai/clay",
    "openai/davinci", "meta/roberta-large", "google/reformer", "facebook/lstm-base",
    "bigscience/mt5-large", "pytorch/fairseq", "facebook/vision-transformer",
    "OpenAI/whisper", "google/retina", "bigscience/bart-large", "microsoft/xlm",
    "OpenAI/gpt-3", "EleutherAI/gpt-neo-x"
]

# Install transformers library if not installed
!pip install transformers

from transformers import AutoModelForCausalLM, AutoTokenizer

# Define function to download models
def download_model(model_name, save_path):
    try:
        # Downloading model and tokenizer
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Saving the model to Google Drive
        model.save_pretrained(save_path)
        tokenizer.save_pretrained(save_path)
        print(f"Successfully downloaded and saved: {model_name}")
    except Exception as e:
        print(f"Error downloading {model_name}: {e}")

# Download each model and save to Google Drive
model_directory = "/content/drive/MyDrive/colab_models"  # Corrected path

for model_name in ai_models:
    save_path = model_directory + model_name.split("/")[-1]  # Saving each model in a specific folder
    download_model(model_name, save_path)
