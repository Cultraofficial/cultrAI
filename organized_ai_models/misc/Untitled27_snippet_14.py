import os
import pyrebase
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM

# Step 1: Set up Google Drive
from google.colab import drive
drive.mount('/content/drive')

project_folder = "/content/drive/My Drive/CultrA.I. Files"
os.makedirs(project_folder, exist_ok=True)
print(f"Project folder ready at: {project_folder}")

# Step 2: Configure Firebase
firebase_config = {
    "apiKey": "YOUR_FIREBASE_API_KEY",
    "authDomain": "YOUR_PROJECT.firebaseapp.com",
    "databaseURL": "https://YOUR_PROJECT.firebaseio.com",
    "storageBucket": "YOUR_PROJECT.appspot.com"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# Step 3: Hugging Face Login
huggingface_token = "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"
login(huggingface_token)

# Step 4: Generate AI Code
def generate_code(task_description):
    model_name = "bigcode/starcoder"  # Replace with your preferred Hugging Face model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Tokenize and generate code
    inputs = tokenizer(task_description, return_tensors="pt", truncation=True)
    outputs = model.generate(inputs["input_ids"], max_length=200, temperature=0.8, do_sample=True, top_p=0.9)

    # Decode and return the generated code
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Step 5: AI Task Execution
task = "Write a Python script to fetch data from an API and store it in Firebase."
print(f"AI Task: {task}")
generated_code = generate_code(task)
print(f"Generated Code:\n{generated_code}")

# Save generated code to Google Drive
generated_code_path = os.path.join(project_folder, "generated_code.py")
with open(generated_code_path, "w") as f:
    f.write(generated_code)
print(f"Generated code saved to: {generated_code_path}")

# Step 6: Log Results to Firebase
db.child("ai_tasks").push({"task": task, "code_path": generated_code_path})
print("Task and code logged to Firebase.")
