# Install whisper if not installed
!pip install git+https://github.com/openai/whisper.git

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
save_directory = "/content/drive/MyDrive/colab_models"

# Function to load each model from the local directory and create the appropriate pipeline
def load_model(model_name, task_type):
    model_path = os.path.join(save_directory, model_name)
    try:
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

        elif task_type == "image-classification":
            model = AutoModelForImageClassification.from_pretrained(model_path)
            return pipeline("image-classification", model=model)

        elif task_type == "whisper":
            # Whisper model for speech-to-text
            whisper_model = whisper.load_model("base")
            return whisper_model

        elif task_type == "sentence-embeddings":
            model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            return pipeline("feature-extraction", model=model, tokenizer=tokenizer)

        else:
            print(f"Task type {task_type} is not recognized.")
            return None
    except Exception as e:
        print(f"Error loading {model_name}: {e}")
        return None

# Define models and their associated task types for loading
models_to_deploy = {
    "cardiffnlp_twitter-roberta-base-sentiment": "sequence-classification",  # Sentiment Analysis
    "EleutherAI_gpt-neo-1.3B": "causal-lm",  # Text Generation
    "facebook_bart-large-cnn": "seq2seq-lm",  # Summarization
    "Salesforce_codegen-350M-mono": "causal-lm",  # Code Generation
    "google_mt5-small": "seq2seq-lm",  # Multilingual Text
    "google_vit-base-patch16-224": "image-classification",  # Image Classification
    "sentence-transformers_all-MiniLM-L6-v2": "sentence-embeddings",  # Sentence Embeddings
    "openai_whisper-base": "whisper"  # Speech-to-Text
}

# Load and initialize all models
loaded_models = {}
for model_name, task_type in models_to_deploy.items():
    print(f"Loading model: {model_name} for task: {task_type}")
    loaded_models[model_name] = load_model(model_name, task_type)

print("All models loaded successfully where possible.")
