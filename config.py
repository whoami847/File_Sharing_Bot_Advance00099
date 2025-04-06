import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Telegram Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TGCrypto = os.getenv("TGCrypto") == "True"  # Convert string 'True'/'False' to boolean
ADMIN_ID = os.getenv("ADMIN_ID")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE")
FILES_PATH = os.getenv("FILES_PATH")
SESSION_NAME = os.getenv("SESSION_NAME")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH")
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")  # Default to DEBUG if not set

# Default configurations
if not TGCrypto:
    TGCrypto = False  # Default to False if not set
