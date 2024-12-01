from transformers import AutoTokenizer, AutoModelForCausalLM

# Load a small Hugging Face model (e.g., GPT-2) for testing
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Generate a response
prompt = "The future of AI is"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(inputs["input_ids"], max_length=50)

# Display response
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
