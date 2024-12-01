from transformers import pipeline

# Load a pipeline for text generation, sentiment analysis, or another task
nlp = pipeline("text-generation", model="gpt2")

# Test the pipeline
result = nlp("Once upon a time,")
print(result)
