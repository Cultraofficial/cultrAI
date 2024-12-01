from pyngrok import ngrok, conf

# Set Ngrok authtoken
ngrok.set_auth_token("2ooma1TJYZL1Mh97aTguEPFVWB1_2B5rAwbuoEGMa1QsqRMRa")

# Start Ngrok
public_url = ngrok.connect(8080)  # Replace 8080 with the port you need
print("Ngrok public URL:", public_url)
