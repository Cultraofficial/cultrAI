from web3 import Web3

# Alchemy HTTP Provider
alchemy_api_url = "https://eth-mainnet.g.alchemy.com/v2/alcht_Wojj6ToT7Y3mDzSGTf91NaSYzieflj"
web3 = Web3(Web3.HTTPProvider(alchemy_api_url))

# Check if the connection is successful
if web3.is_connected():
    print("Connected to Ethereum via Alchemy!")

    # Example: Get the latest block number
    latest_block = web3.eth.block_number
    print(f"Latest Block Number: {latest_block}")
else:
    print("Failed to connect to Alchemy.")
