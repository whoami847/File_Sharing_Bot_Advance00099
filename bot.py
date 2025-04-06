import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_TOKEN, API_ID, API_HASH, ADMIN_USER_ID
from handlers.user_handler import handle_user_commands
from handlers.admin_handler import handle_admin_commands
from handlers.media_handler import handle_media_commands

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the bot client
app = Client("FileSharingBot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Handlers for different user commands
@app.on_message(filters.command(["start", "help"]))
async def start_message(client, message: Message):
    await handle_user_commands(client, message)

@app.on_message(filters.command(["admin", "settings"]) & filters.user(ADMIN_USER_ID))
async def admin_commands(client, message: Message):
    await handle_admin_commands(client, message)

@app.on_message(filters.media)
async def handle_media(client, message: Message):
    await handle_media_commands(client, message)

if __name__ == "__main__":
    app.run()
