from pyngrok import ngrok

# Replace with your Ngrok authtoken
NGROK_AUTH_TOKEN = "2ooma1TJYZL1Mh97aTguEPFVWB1_2B5rAwbuoEGMa1QsqRMRa"
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Open the tunnel
public_url = ngrok.connect(5000)  # Flask will run on port 5000
print("Public URL:", public_url)
