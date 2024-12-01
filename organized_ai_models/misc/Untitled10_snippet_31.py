# Commit and Push Changes to GitHub
os.chdir("sacrifice-in-Cultra")  # Move into the repository directory
!git add .
!git commit -m "Add workflow and training script"

# Use the token in the push URL
repository_push_url = f"https://{github_token}@github.com/Cultraofficial/sacrifice-in-Cultra.git"
!git push {repository_push_url} main
