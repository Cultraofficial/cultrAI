import os
from huggingface_hub import login

# Set the Hugging Face API key as an environment variable
os.environ["HUGGINGFACE_API_KEY"] = "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"  # Replace with your latest key

# Authenticate with Hugging Face
login(os.getenv("HUGGINGFACE_API_KEY"))
print("Authenticated with Hugging Face successfully.")
