from pyrogram import Client, filters
from config import ADMIN_ID

async def admin_handler(client, message):
    if message.from_user.id == ADMIN_ID:
        await message.reply("Welcome, admin!")
    else:
        await message.reply("You are not an admin.")
