from pyrogram import Client, filters
from fancy_font import to_fancy  # Importing the fancy font function
from config import BOT_TOKEN
from handlers import user_handler, admin_handler, media_handler

app = Client("file_sharing_bot", bot_token=BOT_TOKEN)

# Example of using fancy font in a command
@app.on_message(filters.command('start'))
async def start(client, message):
    await message.reply(to_fancy("Welcome to the File Sharing Bot!"))

# Registering user commands
app.add_handler(user_handler)
app.add_handler(admin_handler)
app.add_handler(media_handler)

# Run the bot
app.run()
