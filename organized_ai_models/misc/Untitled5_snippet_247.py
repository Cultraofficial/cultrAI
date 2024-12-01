from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
save_path = "/content/model"

# Load and save the model and tokenizer with the token
tokenizer = AutoTokenizer.from_pretrained(model_name, token=os.environ["HF_TOKEN"])
model = AutoModelForSequenceClassification.from_pretrained(model_name, token=os.environ["HF_TOKEN"])

# Save locally
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)
