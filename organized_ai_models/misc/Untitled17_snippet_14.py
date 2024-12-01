from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Define the correct path to save models in Google Drive (without hyphen in the folder name)
model_directory = '/content/drive/My Drive/colab_models'

# Define the next 25 AI models
next_ai_models = [
    "bigscience/bloom-3B", "EleutherAI/gpt-neo-6B", "facebook/bart-large-xsum",
    "microsoft/deberta-v3-xlarge", "openai/davinci", "facebook/bart-large-mnli",
    "google/bert-large-cased", "facebook/opt-2.7b", "google/reformer",
    "google/t5-v1_1-large", "google/bert-base-uncased", "openai/gpt-3",
    "microsoft/roberta-large", "huggingface/llama-7b", "openai/curie",
    "google/flan-t5-small", "facebook/roberta-large", "EleutherAI/gpt-j",
    "facebook/bart-large-cnn", "deepmind/alphafold", "huggingface/transformer",
    "pytorch/fairseq", "microsoft/xlm-roberta-large", "google/bert-large-uncased",
    "openai/davinci-codex", "deepmind/gato", "stablediffusion-v1-4"
]

# Function to download the models
def download_model(model_name, save_path):
    try:
        # Load the model and tokenizer
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Save the model and tokenizer to the specified path
        model.save_pretrained(save_path)
        tokenizer.save_pretrained(save_path)

        print(f"Successfully downloaded and saved: {model_name}")
    except Exception as e:
        print(f"Failed to download {model_name}: {e}")

# Download models from the list
for model_name in next_ai_models:
    save_path = model_directory + model_name.split("/")[-1]  # Save each model in the specified folder
    download_model(model_name, save_path)
