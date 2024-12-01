# Install pyngrok if not already installed
!pip install -q pyngrok flask

# Import necessary libraries
from flask import Flask
from threading import Thread
from pyngrok import ngrok

# Initialize Flask app
app = Flask(__name__)

# Define a basic route
@app.route("/")
def home():
    return "Hello, World!"

# Function to run the Flask app
def run_flask():
    app.run(host="0.0.0.0", port=5000, threaded=False, use_reloader=False)

# Start the Flask app in a separate thread
flask_thread = Thread(target=run_flask)
flask_thread.start()

# Connect to Ngrok and print the public URL
public_url = ngrok.connect(5000)
print("Public URL:", public_url)
