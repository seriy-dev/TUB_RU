from datetime import datetime
from pyrogram import Client, filters
from helps.modules import add_module, add_command

from helps.get_prefix import get_prefix
prefix = get_prefix()


@Client.on_message(filters.command("ping", prefixes=prefix) & filters.me)
async def ping(client, message):
    start_t = datetime.now()
    await message.edit("🏓")
    end_t = datetime.now()
    time_taken_s = (end_t - start_t).microseconds / 1000
    await message.edit(f"<i>Понг!</i>\n<b>🏓 Пинг равен {round(time_taken_s)}ms</b>")

add_module("ping", __file__)
add_command("ping", f"{prefix}ping", "получить пинг юзербота")