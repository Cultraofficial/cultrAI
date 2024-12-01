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

# Directory where models are saved
save_directory = "/content/drive/MyDrive/colab_models"  # Update path to save models in Google Drive

# Function to load each model from the local directory or download from Hugging Face if needed
def load_model(model_name, task_type):
    model_path = os.path.join(save_directory, model_name)
    try:
        if task_type == "sequence-classification":
            model = AutoModelForSequenceClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

        elif task_type == "causal-lm":
            model = AutoModelForCausalLM.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            return pipeline("text-generation", model=model, tokenizer=tokenizer)

        elif task_type == "seq2seq-lm":
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            return pipeline("summarization", model=model, tokenizer=tokenizer)

        elif task_type == "image-classification":
            model = AutoModelForImageClassification.from_pretrained(model_name)
            return pipeline("image-classification", model=model)

        elif task_type == "whisper":
            whisper_model = whisper.load_model("small")
            return whisper_model

        elif task_type == "sentence-embeddings":
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            return pipeline("feature-extraction", model=model, tokenizer=tokenizer)

        else:
            print(f"Task type {task_type} is not recognized.")
            return None
    except Exception as e:
        print(f"Error loading {model_name}: {e}")
        return None

# Define models and their associated task types for loading
models_to_deploy = {
    "cardiffnlp/twitter-roberta-base-sentiment": "sequence-classification",  # Sentiment Analysis
    "EleutherAI/gpt-neo-1.3B": "causal-lm",  # Text Generation
    "facebook/bart-large-cnn": "seq2seq-lm",  # Summarization
    "Salesforce/codegen-350M-mono": "causal-lm",  # Code Generation
    "google/mt5-small": "seq2seq-lm",  # Multilingual Text
    "microsoft/resnet-50": "image-classification",  # Image Classification Alternative
    "sentence-transformers/paraphrase-MiniLM-L6-v2": "sentence-embeddings",  # Sentence Embeddings Alternative
    "openai/whisper-small": "whisper"  # Speech-to-Text
}

# Load and initialize all models
loaded_models = {}
for model_name, task_type in models_to_deploy.items():
    print(f"Loading model: {model_name} for task: {task_type}")
    loaded_models[model_name] = load_model(model_name, task_type)
    # Save model if loaded successfully
    if loaded_models[model_name] is not None:
        loaded_models[model_name].save_pretrained(os.path.join(save_directory, model_name))
        print(f"Model {model_name} loaded and saved successfully.")
    else:
        print(f"Failed to load model: {model_name}")

print("All models loaded and saved to Google Drive successfully where possible.")
