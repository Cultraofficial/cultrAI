from huggingface_hub import HfApi
from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import torch
import gc

# Use your Hugging Face token for authentication
HUGGING_FACE_TOKEN = "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"  # Automatically applies
api = HfApi(token=HUGGING_FACE_TOKEN)

# Define target download directory in Google Drive
target_dir = "/content/drive/My Drive/Colab_models"

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Define the new high-impact models to download
models_to_download = [
    # High-performance, less common models
    "stabilityai/stablelm-base-alpha-7b",  # Excellent for language understanding and generation
    "EleutherAI/pythia-12b",  # Advanced large language model with optimized training
    "bigscience/T0p",  # Multitask prompt-based model for various NLP tasks
    "carperai/instruct-gpt-neo-20b",  # Fine-tuned model focused on instruction-based tasks
    "mistralai/Mistral-7B",  # New efficient model, highly regarded for its balanced performance
    "togethercomputer/RedPajama-INCITE-7B-Chat",  # Optimized chat model with superior language capability
    "meta-llama/Llama-2-7b-chat-hf",  # Chat-tuned version of LLaMA 2, suited for conversational AI tasks
    "h2oai/h2ogpt-oig-oasst1-256-12b",  # H2O's advanced chatbot model
    "THUDM/glm-10b",  # General Language Model with strong performance on Chinese and English tasks
    "facebook/galactica-6.7b",  # Science-oriented model, excelling in knowledge-intensive tasks
]

# Check for already downloaded models and skip them
downloaded_models = os.listdir(target_dir)
models_to_download = [model for model in models_to_download if model.split("/")[-1] not in downloaded_models]

# Function to clear RAM and disk cache
def clear_cache():
    gc.collect()
    torch.cuda.empty_cache()

# Download each model if not already present
for model_name in models_to_download:
    print(f"Attempting to download {model_name}...")
    try:
        # Load model and tokenizer
        model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=HUGGING_FACE_TOKEN)
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=HUGGING_FACE_TOKEN)

        # Save model to Google Drive
        model_dir = os.path.join(target_dir, model_name.split("/")[-1])
        model.save_pretrained(model_dir)
        tokenizer.save_pretrained(model_dir)

        print(f"Successfully downloaded and saved {model_name}.")

        # Clear cache after saving each model
        del model
        del tokenizer
        clear_cache()

    except Exception as e:
        print(f"Failed to download {model_name}: {e}")
        clear_cache()  # Clear cache even on failure to keep resources free

print("Download process completed.")
