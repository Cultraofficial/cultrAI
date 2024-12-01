from web3 import Web3

# Connect to blockchain via provider
provider_url = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
web3 = Web3(Web3.HTTPProvider(provider_url))

# Generate a temporary wallet
wallet = web3.eth.account.create()
print("Temporary Wallet Address:", wallet.address)

# Fund it, use it, and discard it later
