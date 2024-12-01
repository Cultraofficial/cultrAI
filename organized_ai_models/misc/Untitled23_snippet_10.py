# Install alchemy-sdk (if not already installed in the new runtime)
!pip install alchemy-sdk

# Import Alchemy SDK
from alchemy_sdk import Alchemy, Network

# Your Alchemy API key
api_key = "alcht_Wojj6ToT7Y3mDzSGTf91NaSYzieflj"

# Initialize Alchemy settings
settings = {
    "api_key": api_key,
    "network": Network.ETH_MAINNET  # Connecting to Ethereum Mainnet
}

alchemy = Alchemy(settings)

# Test the connection by fetching the latest block number
try:
    latest_block = alchemy.core.get_block_number()
    print(f"🎉 Connected to Ethereum Mainnet! Latest block number: {latest_block}")
except Exception as e:
    print(f"❌ Failed to connect to Alchemy: {e}")
