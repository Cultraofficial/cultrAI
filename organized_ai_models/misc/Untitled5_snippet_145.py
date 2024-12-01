# Start Flask in a background process
from threading import Thread

def run_flask():
    app.run()

flask_thread = Thread(target=run_flask)
flask_thread.start()

# Start Ngrok after Flask
from pyngrok import ngrok
public_url = ngrok.connect(5000)
print("Public URL:", public_url)
