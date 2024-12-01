from transformers import AutoTokenizer, AutoModelForCausalLM

# Load GPT-2 Model
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Prepare the input
prompt = "The future of AI is"
inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

# Add an attention mask and explicitly set pad_token_id
inputs["attention_mask"] = (inputs["input_ids"] != tokenizer.pad_token_id).long()

# Generate a response
outputs = model.generate(
    inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    max_length=50,
    pad_token_id=tokenizer.eos_token_id
)

# Display the result
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)

# Save response to Google Drive
output_file = "/content/drive/My Drive/CultrA.I. Files/ai_response.txt"
with open(output_file, "w") as f:
    f.write(response)
print(f"Response saved to: {output_file}")
