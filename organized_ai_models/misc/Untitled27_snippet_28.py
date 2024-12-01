from transformers import AutoTokenizer, AutoModelForCausalLM

# Authenticate Hugging Face
HUGGINGFACE_TOKEN = "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"

# Load the model
print("Loading AI model...")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Generate test output
prompt = "The next step for AI-driven automation is"
inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
outputs = model.generate(inputs["input_ids"], max_length=50, pad_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
