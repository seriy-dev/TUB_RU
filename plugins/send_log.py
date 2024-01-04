from pyrogram import Client, filters
from helps.modules import add_module, add_command

from helps.get_prefix import get_prefix
prefix = get_prefix()

@Client.on_message(filters.command("send_log", prefixes=prefix) & filters.me)
async def send_log(client, message):
    try:
        await client.send_document(
            chat_id=message.chat.id,
            document=open("log.log", "rb"),
            caption="<b>Logs TimkaUserBot</b>")
        await message.delete()
    except:
        await message.edit("Лог пустой!")

add_module("send_log", __file__)
add_command("send_log", f"{prefix}send_log", "Отправляет файл с логами")