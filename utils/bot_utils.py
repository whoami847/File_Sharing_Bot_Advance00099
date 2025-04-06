from pyrogram import Client

# Simple function to send message
async def send_message(client: Client, chat_id, text):
    await client.send_message(chat_id, text)
