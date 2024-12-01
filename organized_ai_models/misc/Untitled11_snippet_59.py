import os

# Check disk usage before clearing
!df -h /  # Shows disk usage

# List files larger than 100MB to identify space-consuming files
!find / -type f -size +100M 2>/dev/null

# Delete specific files (replace 'filepath' with the actual path you want to delete)
os.remove('filepath')  # Example: os.remove('/path/to/large/file')
