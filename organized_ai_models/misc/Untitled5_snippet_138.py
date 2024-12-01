# Install Ngrok
!pip install pyngrok

# Import and configure Ngrok
from pyngrok import ngrok

# Set up Ngrok to tunnel Flask's default port (5000)
public_url = ngrok.connect(5000)
print("Flask server is publicly accessible at:", public_url)
