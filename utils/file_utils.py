import os
from pyrogram.types import Message
from config import FILE_DOWNLOAD_PATH

def save_file(message: Message):
    file_id = message.document.file_id if message.document else message.video.file_id
    file_name = message.document.file_name if message.document else f"video_{file_id}.mp4"
    file_path = os.path.join(FILE_DOWNLOAD_PATH, file_name)
    message.download(file_path)
    return file_path
