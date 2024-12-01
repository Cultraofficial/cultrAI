from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

try:
    # Load and save the model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, use_auth_token=True)

    # Define the save path
    save_path = "/content/model"
    os.makedirs(save_path, exist_ok=True)

    # Save locally
    model.save_pretrained(save_path)
    tokenizer.save_pretrained(save_path)

    # Confirm all required files are present
    assert os.path.exists(os.path.join(save_path, "pytorch_model.bin")), "pytorch_model.bin not found"
    print("Model and tokenizer successfully saved.")
except Exception as e:
    print("Error in downloading or saving model:", e)
