app = Flask(__name__)

@app.route('/')
def home():
    return "Cultra Interactive Platform API is running!"

# Start the Flask server
def run_flask():
    app.run(port=5000)

# Start Ngrok to create a public URL
public_url = ngrok.connect(5000)
print("Public URL:", public_url)

# Run the Flask app in a separate thread
import threading
thread = threading.Thread(target=run_flask)
thread.start()
