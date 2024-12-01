# Example Flask server code
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Ngrok!"

app.run(port=5000)
