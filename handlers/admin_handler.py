from pyrogram import Client
from pyrogram.types import Message

async def handle_admin_commands(client: Client, message: Message):
    if message.text.lower() == "/admin":
        await message.reply("Welcome to the Admin Panel! Use the appropriate commands for admin tasks.")
    elif message.text.lower() == "/settings":
        await message.reply("Here you can change bot settings and manage users.")
