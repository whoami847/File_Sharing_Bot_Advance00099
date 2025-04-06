from pyrogram import Client, filters

async def media_handler(client, message):
    if message.photo:
        await message.reply("Nice photo!")
    elif message.video:
        await message.reply("Nice video!")
    else:
        await message.reply("Send a photo or video.")
