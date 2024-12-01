from pyngrok import ngrok

# Open a tunnel to the Flask app
public_url = ngrok.connect(5000)
print("Public URL:", public_url)
