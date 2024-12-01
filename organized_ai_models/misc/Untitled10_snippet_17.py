# List all files in the cloned repository to check directory structure and file names
import os

repo_path = "/content/repo1"

# List all files and directories within the cloned repository
for root, dirs, files in os.walk(repo_path):
    level = root.replace(repo_path, '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    sub_indent = ' ' * 4 * (level + 1)
    for f in files:
        print(f"{sub_indent}{f}")
