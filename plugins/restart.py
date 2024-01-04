from pyrogram import Client, filters
from helps.modules import add_module, add_command
from helps.scripts import restart

from helps.get_prefix import get_prefix
prefix = get_prefix()

@Client.on_message(filters.command("restart", prefix) & filters.me)
async def restart_userbot(_, message):
    await message.edit("<b>Перезагружаю юзербота...</b>")
    await restart(message)

add_module("restart", __file__)
add_command("restart", f"{prefix}restart", "перезапускает юзербота")
