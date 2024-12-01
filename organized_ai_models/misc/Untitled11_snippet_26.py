import os
from google.colab import drive

# Ensure drive is mounted
drive.mount('/content/drive')

# Change directory to your cloned GitHub repo
os.chdir('/content/sacrifice-in-Cultra')

# Create a test file to trigger the GitHub Actions workflow
with open('trigger_workflow.txt', 'w') as f:
    f.write('Testing GitHub Actions workflow for Vertex AI deployment')

# Add, commit, and push the test file to GitHub
!git add trigger_workflow.txt
!git commit -m "Trigger GitHub Actions workflow for Vertex AI deployment"
!git push origin main
