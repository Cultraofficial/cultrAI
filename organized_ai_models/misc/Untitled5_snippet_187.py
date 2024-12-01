import os
import json
import subprocess

# Define all paths, project IDs, and credentials automatically
service_account_path = '/drive/My Drive/BrandNewKey.json'
project_id = 'your_project_id_here'  # Replace with your project ID if known
ngrok_public_url = 'https://6f0e-34-138-79-32.ngrok-free.app'  # Latest Ngrok public URL

# Initialize diagnostics dictionary to store information
diagnostics = {
    "installed_packages": [],
    "environment_variables": {},
    "service_account_path": service_account_path,
    "ngrok_status": None,
    "firebase_status": None,
    "vertex_ai_status": None
}

# Step 1: Check installed packages
try:
    installed_packages = subprocess.check_output(['pip', 'freeze']).decode('utf-8').split('\n')
    diagnostics["installed_packages"] = installed_packages
except Exception as e:
    diagnostics["installed_packages"] = f"Error checking packages: {e}"

# Step 2: Set environment variables for automatic application
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path
os.environ["PROJECT_ID"] = project_id
os.environ["NGROK_PUBLIC_URL"] = ngrok_public_url
diagnostics["environment_variables"] = dict(os.environ)

# Step 3: Check Ngrok status automatically
try:
    ngrok_status = subprocess.check_output(['pgrep', '-f', 'ngrok']).decode('utf-8').strip()
    diagnostics["ngrok_status"] = "Running" if ngrok_status else "Not running"
except Exception as e:
    diagnostics["ngrok_status"] = f"Ngrok check error: {e}"

# Step 4: Firebase Connection Check
try:
    import firebase_admin
    from firebase_admin import credentials

    # Initialize Firebase app using automatically applied service account
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)
    diagnostics["firebase_status"] = "Connected"
except Exception as e:
    diagnostics["firebase_status"] = f"Firebase connection error: {e}"

# Step 5: Vertex AI Connection Check
try:
    from google.cloud import aiplatform

    # Initialize Vertex AI with automatic project ID
    aiplatform.init(project=os.environ["PROJECT_ID"])
    diagnostics["vertex_ai_status"] = "Connected"
except Exception as e:
    diagnostics["vertex_ai_status"] = f"Vertex AI connection error: {e}"

# Print diagnostics for review
print(json.dumps(diagnostics, indent=4))
