# Install pyngrok if not already installed
!pip install -q pyngrok flask

# Import necessary libraries
from flask import Flask
from threading import Thread
from pyngrok import ngrok
import socket

# Initialize Flask app
app = Flask(__name__)

# Define a basic route
@app.route("/")
def home():
    return "Hello, World!"

# Function to find an available port
def find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

# Find an available port
port = find_free_port()

# Function to run the Flask app
def run_flask():
    app.run(host="0.0.0.0", port=port, threaded=False, use_reloader=False)

# Start the Flask app in a separate thread
flask_thread = Thread(target=run_flask)
flask_thread.start()

# Connect to Ngrok and print the public URL
public_url = ngrok.connect(port)
print("Public URL:", public_url)
print("Flask app running on port:", port)
