# Step 1: Import required libraries
import os
from google.colab import auth
from google.cloud import storage, aiplatform
from google.cloud import container_v1
from google.cloud import firestore

# Step 2: Authenticate with Google Cloud
auth.authenticate_user()

# Step 3: Set environment variables
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"  # Update path if needed
project_id = "cultra-2ffad"  # Replace with your project ID
cluster_name = "your-cluster-name"  # Replace with your GKE cluster name
zone = "us-central1-a"  # Replace with the correct zone for your cluster

# Step 4: Initialize Google Cloud Platform services
aiplatform.init(project=project_id)

# Step 5: Verify authentication and list available models (optional step)
try:
    models = aiplatform.Model.list()
    print("Available models:", models)
except Exception as e:
    print("Error accessing models:", e)

# Step 6: Connect to the GKE cluster
!gcloud container clusters get-credentials {cluster_name} --zone {zone} --project {project_id}

# Step 7: Apply the YAML configuration file to the GKE cluster
yaml_path = "/content/drive/My Drive/service-account-key.yaml"  # Update path if needed

# Applying the YAML file to the Kubernetes cluster
try:
    !kubectl apply -f {yaml_path}
    print("YAML file applied successfully.")
except Exception as e:
    print("Error applying YAML file:", e)

# Step 8: Verify the service account setup
!kubectl get serviceaccounts
