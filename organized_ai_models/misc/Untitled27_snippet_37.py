# Step 1: Import Libraries
from google.colab import drive
import requests
import pyrebase
import boto3
import schedule
import time
import os
from transformers import AutoTokenizer, AutoModelForCausalLM

# Step 2: Mount Google Drive
drive.mount('/content/drive', force_remount=True)
project_path = '/content/drive/My Drive/CultrA.I. Files'
os.makedirs(project_path, exist_ok=True)
print(f"Project folder ready at: {project_path}")

# Step 3: Firebase Configuration
firebase_config = {
    "apiKey": "YOUR_FIREBASE_API_KEY",
    "authDomain": "YOUR_FIREBASE_AUTH_DOMAIN",
    "databaseURL": "YOUR_FIREBASE_DATABASE_URL",
    "storageBucket": "YOUR_FIREBASE_STORAGE_BUCKET"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()
print("Firebase initialized successfully!")

# Step 4: AWS S3 Configuration
aws_access_key = "8f26f34a47c1613c625ca89554d8dc49"
aws_secret_key = "212cb29a93678cb12e3711ad1315de7d58321342440b04fcaa91f5f733bebe9c"

try:
    s3 = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
    )
    # List available buckets to auto-detect configuration
    response = s3.list_buckets()
    buckets = [bucket["Name"] for bucket in response["Buckets"]]
    if buckets:
        aws_bucket_name = buckets[0]
        print(f"Detected S3 Bucket: {aws_bucket_name}")
    else:
        raise ValueError("No S3 buckets found. Falling back to Firebase.")
except Exception as e:
    print(f"Error configuring S3: {e}")
    aws_bucket_name = None

# Step 5: Load AI Model
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
print("AI model loaded successfully!")

# Step 6: Functions
def fetch_and_store(api_url, node_name):
    try:
        # Fetch data from API
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # Store in Firebase
        db.child(node_name).set(data)
        print(f"Data from {api_url} successfully stored in Firebase under node '{node_name}'!")

        # Store in S3 if available
        if aws_bucket_name:
            s3.put_object(
                Bucket=aws_bucket_name,
                Key=f"{node_name}.json",
                Body=str(data),
            )
            print(f"Data from {api_url} successfully stored in S3 as '{node_name}.json'!")

        # Backup to Google Drive
        with open(os.path.join(project_path, f"{node_name}.json"), "w") as file:
            file.write(str(data))
        print(f"Data from {api_url} successfully backed up to Google Drive as '{node_name}.json'!")

    except Exception as e:
        print(f"Error fetching or storing data: {e}")

def generate_idea(prompt, file_name="ai_ideas.txt"):
    try:
        # Generate text with AI
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
        outputs = model.generate(inputs["input_ids"], max_length=100, pad_token_id=tokenizer.eos_token_id)
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Generated Text:\n{generated_text}")

        # Save text to Firebase
        db.child("ai_generated_ideas").push({"prompt": prompt, "output": generated_text})
        print(f"Generated text successfully stored in Firebase!")

        # Backup to Google Drive
        with open(os.path.join(project_path, file_name), "a") as file:
            file.write(generated_text + "\n")
    except Exception as e:
        print(f"Error generating text: {e}")

# Step 7: Master Task
def master_task():
    print("Starting Master Task...")
    fetch_and_store("https://jsonplaceholder.typicode.com/todos/1", "api_data_1")
    fetch_and_store("https://jsonplaceholder.typicode.com/todos/2", "api_data_2")
    generate_idea("Describe how AI can improve interactive platforms.", "ai_ideas.txt")
    print("Master Task Completed!")

# Step 8: Scheduler
schedule.every(1).hours.do(master_task)

print("Starting the scheduler...")
while True:
    schedule.run_pending()
    time.sleep(1)
