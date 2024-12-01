try:
    from alchemy_sdk import Alchemy, Network
    print("alchemy-sdk imported successfully!")
except ModuleNotFoundError:
    print("alchemy-sdk is not installed or recognized!")
