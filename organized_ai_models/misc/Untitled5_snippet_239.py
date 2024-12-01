from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

# Define model name
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create a directory to save the model
save_path = "/content/model"
os.makedirs(save_path, exist_ok=True)

# Save the model and tokenizer
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)

# Verify that the 'pytorch_model.bin' file exists
assert os.path.exists(os.path.join(save_path, "pytorch_model.bin")), "Model file not found!"
print("Model and tokenizer saved successfully.")
