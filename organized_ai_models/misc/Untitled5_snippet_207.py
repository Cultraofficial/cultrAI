from transformers import pipeline

# Load a Hugging Face model, like sentiment-analysis
sentiment_analyzer = pipeline("sentiment-analysis")

# Test the model with sample text
test_result = sentiment_analyzer("This is a test to confirm deployment.")
print(test_result)
