# Install Alchemy SDK if not already installed
!pip install alchemy-sdk

# Import Alchemy SDK
from alchemy_sdk import Network, Alchemy

# Your Alchemy API key
api_key = "alcht_Wojj6ToT7Y3mDzSGTf91NaSYzieflj"

# Initialize Alchemy with API key and network
settings = {
    "api_key": api_key,
    "network": Network.ETH_MAINNET  # Using Ethereum Mainnet
}

alchemy = Alchemy(settings)

# Test the connection by fetching the latest block number
try:
    latest_block = alchemy.core.get_block_number()
    print(f"🎉 Connected to Ethereum Mainnet! Latest block number: {latest_block}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
