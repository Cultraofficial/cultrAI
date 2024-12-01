from transformers import AutoTokenizer, AutoModelForCausalLM

# Hugging Face Authentication Token
HUGGINGFACE_TOKEN = "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"

# Load the tokenizer and model
print("Loading AI model...")
tokenizer = AutoTokenizer.from_pretrained("gpt2", token=HUGGINGFACE_TOKEN)
model = AutoModelForCausalLM.from_pretrained("gpt2", token=HUGGINGFACE_TOKEN)

# Add a pad_token if not present
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': tokenizer.eos_token})
    model.resize_token_embeddings(len(tokenizer))

# Generate test output
prompt = "The next step for AI-driven automation is"
inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
outputs = model.generate(inputs["input_ids"], max_length=50, pad_token_id=tokenizer.pad_token_id)

# Print the AI-generated output
print("Generated Output:")
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
