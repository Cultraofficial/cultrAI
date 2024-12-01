from web3 import Web3

# Connect to the blockchain (use your temporary wallet)
wallet_address = "0x7be5D5Eae986E8c5f4c920C0b1A0Af5D88EB54dc"
alchemy_api_url = "https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY"

web3 = Web3(Web3.HTTPProvider(alchemy_api_url))

if web3.isConnected():
    print(f"Connected to Ethereum Network. Wallet: {wallet_address}")

    # Fetch all transactions related to the wallet
    transactions = web3.eth.get_transaction_by_block("latest", True)
    for tx in transactions:
        if tx['to'] == wallet_address.lower():
            print(f"Received {tx['value']} wei from {tx['from']}")
            # Logic to extract and consolidate "dust" tokens
else:
    print("Failed to connect to Ethereum.")
