from pyrogram import Client, filters
from fancy_font import to_fancy

@Client.on_message(filters.command('ban'))
async def ban_user(client, message):
    if message.from_user.id == ADMIN_ID:
        # Logic to ban a user
        await message.reply(to_fancy("User has been banned"))
