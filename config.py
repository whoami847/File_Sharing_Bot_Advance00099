import os
from dotenv import load_dotenv

# .env ফাইল থেকে পরিবেশগত ভেরিয়েবল লোড করুন
load_dotenv()

# এখন আপনি পরিবেশগত ভেরিয়েবলগুলো ব্যবহার করতে পারবেন
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TGCrypto = os.getenv("TGCrypto")
ADMIN_ID = os.getenv("ADMIN_ID")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE")
FILES_PATH = os.getenv("FILES_PATH")
SESSION_NAME = os.getenv("SESSION_NAME")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH")
LOG_LEVEL = os.getenv("LOG_LEVEL")

# Default configurations
if not TGCrypto:
    TGCrypto = False  # Default to False if not set
