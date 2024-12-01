# Install web3
!pip install web3 --upgrade --force-reinstall

from web3 import Web3

# Connect directly to Alchemy via HTTPProvider
alchemy_api_url = "https://eth-mainnet.alchemyapi.io/v2/alcht_Wojj6ToT7Y3mDzSGTf91NaSYzieflj"
web3 = Web3(Web3.HTTPProvider(alchemy_api_url))

# Check connection
if web3.isConnected():
    print("Connected to Ethereum via Alchemy!")

    # Example: Get the latest block number
    latest_block = web3.eth.block_number
    print(f"Latest Block Number: {latest_block}")
else:
    print("Failed to connect to Alchemy.")
