from pyrogram import Client, filters
from fancy_font import to_fancy

@Client.on_message(filters.command('encode'))
async def encode_video(client, message):
    # Logic for video encoding
    await message.reply(to_fancy("Video encoding started..."))
