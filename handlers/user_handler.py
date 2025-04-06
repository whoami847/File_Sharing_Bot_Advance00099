from pyrogram import Client, filters

async def user_handler(client, message):
    if message.text == "/help":
        await message.reply("How can I assist you?")
    else:
        await message.reply("Send /help for assistance.")
