from pyrogram import Client, filters
from fancy_font import to_fancy  # Using fancy font conversion

@Client.on_message(filters.command('myfiles'))
async def my_files(client, message):
    user_id = message.from_user.id
    # Logic to list files for the user
    await message.reply(to_fancy(f"Your files, {user_id}: ..."))
