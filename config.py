import os

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID"))

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI")

# Other Configurations
FILE_DOWNLOAD_PATH = "./downloads"
