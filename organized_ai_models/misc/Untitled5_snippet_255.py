sentiment_pipeline = pipeline("sentiment-analysis")
generation_pipeline = pipeline("text-generation", model="gpt2")

# Testing sentiment analysis
sentiment_result = sentiment_pipeline("I am thrilled to be working with Hugging Face!")
print(sentiment_result)

# Testing text generation
generation_result = generation_pipeline("The future of AI is", max_length=50, num_return_sequences=2)
print(generation_result)
