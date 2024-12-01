from web3 import Web3

# Alchemy API URL
alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/alcht_Wojj6ToT7Y3mDzSGTf91NaSYzieflj"
web3 = Web3(Web3.HTTPProvider(alchemy_url))

# Test the connection
if web3.is_connected():
    print("✅ Connected to Ethereum blockchain via Alchemy!")
else:
    print("❌ Connection failed. Please check your API key or URL.")
