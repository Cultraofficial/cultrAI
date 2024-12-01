from pyngrok import ngrok

# Open a new tunnel
ngrok_tunnel = ngrok.connect(5000)
ngrok_url = ngrok_tunnel.public_url
print(f"New Public URL: {ngrok_url}")
