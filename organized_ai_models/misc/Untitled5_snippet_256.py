from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = Flask(__name__)

# Load Hugging Face model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    user_input = request.json['text']
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model(**inputs)
    sentiment = torch.softmax(outputs.logits, dim=1)
    response = {
        "label": "POSITIVE" if sentiment[0][1] > sentiment[0][0] else "NEGATIVE",
        "score": sentiment.max().item()
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
