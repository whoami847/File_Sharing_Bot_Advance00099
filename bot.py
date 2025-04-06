from pyrogram import Client, filters
from fancy_font import to_fancy  # Importing the fancy font function
from config import BOT_TOKEN  # Import the bot token from config
from handlers import user_handler, admin_handler, media_handler  # Import handlers

# Initialize the bot with the provided token and configurations
app = Client("file_sharing_bot", bot_token=BOT_TOKEN, api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH"))

# Example of using fancy font in a command
@app.on_message(filters.command('start'))
async def start(client, message):
    await message.reply(to_fancy("Welcome to the File Sharing Bot!"))

# Registering user, admin, and media handlers
app.add_handler(user_handler)
app.add_handler(admin_handler)
app.add_handler(media_handler)

# Run the bot
app.run()
