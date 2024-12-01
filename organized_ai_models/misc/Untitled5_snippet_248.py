from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
save_path = "/content/model"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name, token=os.environ["HF_TOKEN"])
model = AutoModelForSequenceClassification.from_pretrained(model_name, token=os.environ["HF_TOKEN"])

# Save locally
tokenizer.save_pretrained(save_path)
model.save_pretrained(save_path)

# Verify that the model file exists
assert os.path.exists(os.path.join(save_path, "pytorch_model.bin")), "Model file not found!"
print("Model and tokenizer saved successfully.")
