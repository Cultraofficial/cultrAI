from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
save_path = "/content/model"
hf_token = "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"  # Replace with your active token if needed

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token, revision="main")
model = AutoModelForSequenceClassification.from_pretrained(model_name, use_auth_token=hf_token, revision="main")

# Save locally
tokenizer.save_pretrained(save_path)
model.save_pretrained(save_path)

# Verify that the model file exists
assert os.path.exists(os.path.join(save_path, "pytorch_model.bin")), "Model file not found!"
print("Model and tokenizer saved successfully.")
