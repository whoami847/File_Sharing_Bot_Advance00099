from pyrogram import Client
from pyrogram.types import Message

async def handle_user_commands(client: Client, message: Message):
    if message.text.lower() == "/start":
        await message.reply("Welcome to the File Sharing Bot! Please use the commands to upload, download, and manage your files.")
    elif message.text.lower() == "/help":
        await message.reply("Send your files, and I will handle them. You can download files using special links.")
