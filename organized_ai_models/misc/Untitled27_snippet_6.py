# Install the Hugging Face CLI tool
!pip install huggingface-hub --quiet

# Hugging Face API tokens
huggingface_token_newest = "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"

# Login to Hugging Face
from huggingface_hub import login
login(huggingface_token_newest)

# Test the setup with a small model to ensure the token works
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"  # Using a small model for testing
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Generate a test response
prompt = "The future of AI is"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0]))
