import os

# Specify the path to the cloned repository
repo_path = "/content/repo1"

# List all files and folders within the cloned repository
if os.path.exists(repo_path):
    for root, dirs, files in os.walk(repo_path):
        for name in files:
            print(os.path.join(root, name))
else:
    print("The repository folder does not exist.")
