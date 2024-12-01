# Authenticate with Hugging Face
from huggingface_hub import login

# Use the newest token provided
login("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")

# Load and save the Hugging Face model and tokenizer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

# Define model name
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

try:
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Create a directory to save the model
    save_path = "/content/model"
    os.makedirs(save_path, exist_ok=True)

    # Save the model and tokenizer
    model.save_pretrained(save_path)
    tokenizer.save_pretrained(save_path)

    # Check if the required files exist
    assert os.path.exists(os.path.join(save_path, "pytorch_model.bin")), "pytorch_model.bin not found"
    assert os.path.exists(os.path.join(save_path, "config.json")), "config.json not found"
    assert os.path.exists(os.path.join(save_path, "vocab.txt")), "vocab.txt not found"

    print("Model and tokenizer files saved successfully.")
except Exception as e:
    print("Error during model download or save:", e)
