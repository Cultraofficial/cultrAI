from transformers import AutoTokenizer, AutoModelForCausalLM

# Load an open-source model for code generation
model_name = "codeparrot/codeparrot-small"  # Open-source alternative
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define the coding task
task_description = """# Write a Python script to fetch data from an API and store it in Firebase"""

# Tokenize and generate code
inputs = tokenizer(task_description, return_tensors="pt", truncation=True)
outputs = model.generate(
    inputs["input_ids"],
    max_length=150,
    temperature=0.7,
    top_k=50,
    top_p=0.9,
    do_sample=True
)

# Decode and print the generated code
generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(f"Generated Code:\n{generated_code}")

# Save generated code to Google Drive
output_file = "/content/drive/My Drive/CultrA.I. Files/generated_code.py"
with open(output_file, "w") as f:
    f.write(generated_code)
print(f"Generated code saved to: {output_file}")
