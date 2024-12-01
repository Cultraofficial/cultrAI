from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSeq2SeqLM
import os

# Correct directory for saving models
model_directory = "/content/drive/MyDrive/colab_models"

# List of models to download (first 50 models for testing)
next_ai_models = [
    "EleutherAI/gpt-neo-2.7B", "EleutherAI/gpt-neo-1.3B", "bigscience/bloom-560m",
    "facebook/bart-large-cnn", "bert-base-uncased", "google/flan-t5-xxl", "facebook/bart-large-xsum",
    "google/bert-base-cased", "openai/gpt-3", "bigscience/bloom-1b7", "EleutherAI/gpt-j",
    "t5-base", "google/t5-xxl", "huggingface/transformer-model", "bert-large-uncased",
    "t5-small", "facebook/bart-large", "microsoft/deberta-v3-base", "facebook/roberta-large",
    "mistral-7B", "google/bert-large-cased", "openai/codex", "openai/davinci",
    "mistral-7b", "turing-gpt", "huggingface/bert", "EleutherAI/gpt-neoX-20B",
    "google/mt5", "h2oai/llama", "EleutherAI/gpt-neo-350M", "facebook/bart-large-mnli",
    "google/bert-large", "EleutherAI/robust-gpt2", "facebook/bart-base",
    "h2oai/transformers", "openai/codex-davinci", "eleutherai/dolly-2", "openai/whisper",
    "openai/cliptok", "perceiver-io", "EleutherAI/gpt-j-6B", "turing-nlg", "bigscience/bloom",
    "facebook/mistral", "google/t5-multilingual", "EleutherAI/gpt-neo-125M", "mistral/7B",
    "gpt-2", "openai/cliptok", "turing-nlg2", "flan", "bert-base-cased"
]

# Function to download the models
def download_model(model_name, save_path):
    print(f"Downloading {model_name}...")
    try:
        # Use AutoModelForSeq2SeqLM for Seq2Seq models like FLAN
        if "flan" in model_name.lower():
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        else:
            model = AutoModelForCausalLM.from_pretrained(model_name)

        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Save the model and tokenizer
        model.save_pretrained(save_path)
        tokenizer.save_pretrained(save_path)
        print(f"Model {model_name} saved to {save_path}")
    except Exception as e:
        print(f"Failed to download {model_name}. Error: {str(e)}")

# Download the models
for model_name in next_ai_models:
    save_path = model_directory + model_name.split("/")[-1]  # Save in colab_models directory
    download_model(model_name, save_path)
