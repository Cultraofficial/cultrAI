!pip install transformers openai-whisper
from transformers import (
    AutoModelForSequenceClassification,
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    AutoModelForImageClassification,
    pipeline
)
import whisper
import os

# Directory to save models to Google Drive
save_directory = "/content/drive/MyDrive/colab_models"

# Function to download, load, and save each model to Google Drive
def load_and_save_model(model_name, task_type):
    try:
        if task_type == "sequence-classification":
            model = AutoModelForSequenceClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            pipeline_model = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

        elif task_type == "causal-lm":
            model = AutoModelForCausalLM.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            pipeline_model = pipeline("text-generation", model=model, tokenizer=tokenizer)

        elif task_type == "seq2seq-lm":
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            pipeline_model = pipeline("summarization", model=model, tokenizer=tokenizer)

        elif task_type == "image-classification":
            model = AutoModelForImageClassification.from_pretrained(model_name)
            pipeline_model = pipeline("image-classification", model=model)

        elif task_type == "whisper":
            whisper_model = whisper.load_model("base")
            return whisper_model

        elif task_type == "sentence-embeddings":
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            pipeline_model = pipeline("feature-extraction", model=model, tokenizer=tokenizer)

        else:
            print(f"Task type {task_type} is not recognized.")
            return None

        # Save model to Google Drive
        model.save_pretrained(os.path.join(save_directory, model_name))
        tokenizer.save_pretrained(os.path.join(save_directory, model_name))
        print(f"Model {model_name} loaded and saved successfully.")

        return pipeline_model

    except Exception as e:
        print(f"Error loading {model_name}: {e}")
        return None

# Define models and their associated task types for loading
models_to_deploy = {
    "cardiffnlp/twitter-roberta-base-sentiment": "sequence-classification",
    "EleutherAI/gpt-neo-1.3B": "causal-lm",
    "facebook/bart-large-cnn": "seq2seq-lm",
    "Salesforce/codegen-350M-mono": "causal-lm",
    "google/mt5-small": "seq2seq-lm",
    "google/vit-base-patch16-224": "image-classification",
    "sentence-transformers/all-MiniLM-L6-v2": "sentence-embeddings",
    "openai/whisper-small": "whisper"
}

# Load and initialize all models
loaded_models = {}
for model_name, task_type in models_to_deploy.items():
    print(f"Loading model: {model_name} for task: {task_type}")
    loaded_models[model_name] = load_and_save_model(model_name, task_type)

print("All models loaded and saved to Google Drive successfully where possible.")
