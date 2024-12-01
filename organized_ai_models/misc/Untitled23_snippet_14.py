from alchemy_sdk import Alchemy, Network
from web3 import Web3

# Automatically applying your API key
api_key = "alcht_Wojj6ToT7Y3mDzSGTf91NaSYzieflj"

# Initialize Alchemy SDK
alchemy = Alchemy(api_key=api_key, network=Network.ETH_MAINNET)

# Initialize Web3 connection using Alchemy
alchemy_url = f"https://eth-mainnet.g.alchemy.com/v2/{api_key}"
web3 = Web3(Web3.HTTPProvider(alchemy_url))

try:
    # Test connection
    if web3.is_connected():
        print("Connected to Ethereum network!")

        # Fetch the latest block using both Alchemy and Web3
        latest_block_alchemy = alchemy.core.get_block("latest")
        latest_block_web3 = web3.eth.get_block('latest')

        print(f"Latest block (Alchemy): {latest_block_alchemy}")
        print(f"Latest block (Web3): {latest_block_web3}")
    else:
        print("Failed to connect to the Ethereum network.")
except Exception as e:
    print(f"Error: {e}")
