import os
import shutil
from transformers import (
    AutoModelForSequenceClassification,
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    pipeline
)
import whisper

# Set up Google Drive for saving models
drive_model_directory = "/content/drive/MyDrive/colab_models"  # Folder in Google Drive to store models
os.makedirs(drive_model_directory, exist_ok=True)

# Function to load and save each model to Google Drive
def load_and_save_model(model_name, task_type):
    model_path = os.path.join(drive_model_directory, model_name.replace("/", "_"))

    # If the model is already saved in Google Drive, load from there
    if os.path.exists(model_path):
        print(f"Loading {model_name} from Google Drive.")
        if task_type == "sequence-classification":
            model = AutoModelForSequenceClassification.from_pretrained(model_path)
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

        elif task_type == "causal-lm":
            model = AutoModelForCausalLM.from_pretrained(model_path)
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            return pipeline("text-generation", model=model, tokenizer=tokenizer)

        elif task_type == "seq2seq-lm":
            model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            return pipeline("summarization", model=model, tokenizer=tokenizer)

        elif task_type == "whisper":
            whisper_model = whisper.load_model("small")
            return whisper_model

    # If not saved, download, save to Google Drive, and load
    else:
        print(f"Downloading and saving {model_name} to Google Drive.")
        if task_type == "sequence-classification":
            model = AutoModelForSequenceClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model.save_pretrained(model_path)
            tokenizer.save_pretrained(model_path)
            return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

        elif task_type == "causal-lm":
            model = AutoModelForCausalLM.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model.save_pretrained(model_path)
            tokenizer.save_pretrained(model_path)
            return pipeline("text-generation", model=model, tokenizer=tokenizer)

        elif task_type == "seq2seq-lm":
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model.save_pretrained(model_path)
            tokenizer.save_pretrained(model_path)
            return pipeline("summarization", model=model, tokenizer=tokenizer)

        elif task_type == "whisper":
            whisper_model = whisper.load_model("small")
            whisper_model_dir = os.path.join(drive_model_directory, "whisper_small")
            os.makedirs(whisper_model_dir, exist_ok=True)
            # Save Whisper model weights manually
            whisper_model.save(whisper_model_dir)  # Specific save function if available
            return whisper_model

# Example models to load and save
models_to_save = {
    "cardiffnlp/twitter-roberta-base-sentiment": "sequence-classification",
    "EleutherAI/gpt-neo-1.3B": "causal-lm",
    "facebook/bart-large-cnn": "seq2seq-lm",
    "openai/whisper-small": "whisper"
}

# Load and save each model
loaded_models = {}
for model_name, task_type in models_to_save.items():
    loaded_models[model_name] = load_and_save_model(model_name, task_type)

print("All models loaded and saved to Google Drive successfully where possible.")
