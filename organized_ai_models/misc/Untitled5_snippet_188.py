# Install ngrok
!pip install pyngrok

# Start ngrok
from pyngrok import ngrok

# Open a new public URL
public_url = ngrok.connect(8080)  # Replace 8080 with the port you need
print("Ngrok public URL:", public_url)
