# Install necessary dependencies
!pip install web3 requests pandas matplotlib

from web3 import Web3
import os

# Automatically select provider (Alchemy or Infura)
USE_ALCHEMY = True  # Set to False if using Infura

# Set your keys (automatically applied if given)
ALCHEMY_API_URL = "https://eth-mainnet.g.alchemy.com/v2/alcht_Tkj0njdooRLwRT5XxQkOpzXpMpw9TA"
INFURA_API_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY"

# Auto-switch provider
API_URL = ALCHEMY_API_URL if USE_ALCHEMY else INFURA_API_URL

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(API_URL))

# Function to test connection
def test_connection():
    try:
        if web3.is_connected():
            print(f"✅ Connected to Ethereum blockchain via {'Alchemy' if USE_ALCHEMY else 'Infura'}!")
        else:
            raise ConnectionError("❌ Connection failed. Please check your API key or URL.")
    except Exception as e:
        print(f"Connection Error: {e}")

# Function to fetch blockchain data
def fetch_blockchain_data():
    try:
        print("🔄 Fetching blockchain data...")
        # Get the latest block number
        latest_block = web3.eth.block_number
        print(f"📦 Latest Block Number: {latest_block}")

        # Example: Fetch ETH balance of a wallet
        sample_wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Replace with any wallet address
        balance = web3.eth.get_balance(sample_wallet)
        eth_balance = web3.from_wei(balance, "ether")
        print(f"💰 ETH Balance for Wallet {sample_wallet}: {eth_balance} ETH")
    except Exception as e:
        print(f"Error fetching blockchain data: {e}")

# Function to automate everything
def automate_setup():
    print("🤖 Setting up blockchain connection...")
    test_connection()
    fetch_blockchain_data()

# Run automation
if __name__ == "__main__":
    automate_setup()
