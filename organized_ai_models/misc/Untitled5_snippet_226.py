from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Save the model locally
model.save_pretrained("/content/model")
tokenizer.save_pretrained("/content/model")
print("Model downloaded and saved locally.")
