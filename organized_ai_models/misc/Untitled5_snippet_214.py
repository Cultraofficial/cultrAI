from transformers import pipeline

# Load a model by name
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
print(sentiment_model("This project is exciting!"))
