from flask import Flask
from threading import Thread
from pyngrok import ngrok

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

# Function to run Flask in a separate thread
def run_flask():
    app.run(threaded=False, use_reloader=False)

# Start Flask and Ngrok
flask_thread = Thread(target=run_flask)
flask_thread.start()

# Connect to Ngrok after starting Flask
public_url = ngrok.connect(5000)
print("Public URL:", public_url)
