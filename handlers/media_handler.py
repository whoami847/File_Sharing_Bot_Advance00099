from pyrogram import Client
from pyrogram.types import Message

async def handle_media_commands(client: Client, message: Message):
    if message.video:
        await message.reply("Video received. I will process it shortly.")
    elif message.document:
        await message.reply("Document received. Processing file.")
