from transformers import AutoTokenizer, AutoModelForCausalLM

# Load a lightweight GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Add a pad_token to the tokenizer
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Prepare the input
prompt = "The future of AI involves breakthroughs in"
inputs = tokenizer(
    prompt,
    return_tensors="pt",
    padding=True,
    truncation=True,
    max_length=50
)

# Generate a response with sampling controls
outputs = model.generate(
    inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    max_length=100,
    pad_token_id=tokenizer.pad_token_id,
    temperature=0.8,  # Controls randomness (lower = less random)
    top_k=50,         # Limits sampling to top 50 tokens for diversity
    top_p=0.9         # Nucleus sampling for higher-quality outputs
)

# Display the result
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)

# Save response to Google Drive
output_file = "/content/drive/My Drive/CultrA.I. Files/ai_response.txt"
with open(output_file, "w") as f:
    f.write(response)
print(f"Response saved to: {output_file}")
