# Install necessary dependencies
!pip install web3 requests pandas matplotlib

# Import required libraries
from web3 import Web3
import requests

# Your Alchemy API Key and URL
ALCHEMY_API_URL = "https://eth-mainnet.g.alchemy.com/v2/alcht_Tkj0njdooRLwRT5XxQkOpzXpMpw9TA"

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(ALCHEMY_API_URL))

# Test the connection
def test_connection():
    try:
        if web3.is_connected():
            print("✅ Successfully connected to Ethereum blockchain via Alchemy!")
        else:
            print("❌ Connection failed. Please check your API key or URL.")
    except Exception as e:
        print(f"Error: {e}")

# Fetch Blockchain Data
def fetch_blockchain_data():
    try:
        print("🔄 Fetching blockchain data...")
        # Example: Get the latest block number
        latest_block = web3.eth.block_number
        print(f"📦 Latest Block Number: {latest_block}")

        # Example: Fetch ETH balance of a wallet
        sample_wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Replace with any wallet address
        balance = web3.eth.get_balance(sample_wallet)
        eth_balance = web3.from_wei(balance, "ether")
        print(f"💰 ETH Balance for Wallet {sample_wallet}: {eth_balance} ETH")
    except Exception as e:
        print(f"Error fetching blockchain data: {e}")

# Main Execution
if __name__ == "__main__":
    test_connection()
    fetch_blockchain_data()
