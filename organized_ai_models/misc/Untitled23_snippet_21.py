from alchemy_sdk import Alchemy, Network
from web3 import Web3

# Automatically applying your API key
api_key = "alcht_Wojj6ToT7Y3mDzSGTf91NaSYzieflj"

# Initialize Alchemy connection
alchemy = Alchemy(api_key=api_key, network=Network.ETH_MAINNET)

# Initialize Web3 connection via Alchemy
web3 = Web3(Web3.HTTPProvider(f"https://eth-mainnet.alchemyapi.io/v2/{api_key}"))

# Test the connection
if web3.isConnected():
    print("Successfully connected to Ethereum via Alchemy!")
else:
    print("Connection to Ethereum via Alchemy failed.")
