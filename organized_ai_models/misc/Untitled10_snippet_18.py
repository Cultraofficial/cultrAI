import subprocess

# Define the GitHub repositories you want to clone
repositories = [
    "REPO_URL_1",
    "REPO_URL_2"
]

# Clone each repository and check if they were cloned successfully
for repo_url in repositories:
    try:
        result = subprocess.run(["git", "clone", repo_url], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully cloned repository: {repo_url}")
        else:
            print(f"Failed to clone repository: {repo_url}")
            print(result.stderr)  # Print error message if cloning fails
    except Exception as e:
        print(f"An error occurred while cloning {repo_url}: {e}")

# Check if the folders exist after cloning
for i, repo_url in enumerate(repositories, 1):
    repo_name = f"repo{i}"  # Replace 'repo1', 'repo2' if they have specific names
    if os.path.exists(f"/content/{repo_name}"):
        print(f"{repo_name} exists and is ready.")
    else:
        print(f"{repo_name} does not exist, cloning might have failed.")
