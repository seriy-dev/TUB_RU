from pyrogram import Client, filters
from helps.modules import add_module, add_command
from helps.scripts import restart, get_lang
from helps.get_prefix import get_prefix

lang = get_lang()
prefix = get_prefix()

class Texts:
    @staticmethod
    def get_texts():
        return {"restart": {
            "ru": f"<b>Перезагружаю юзербота...</b>",
            "en": f"<b>Restarting the userbot...</b>"
        }
        }

@Client.on_message(filters.command("restart", prefix) & filters.me)
async def restart_userbot(_, message):
    text_versions = Texts.get_texts()

    await message.edit(text_versions["restart"][lang])
    await restart(message)


if lang == "ru":
    add_module("restart", __file__)
    add_command("restart", f"{prefix}restart", "перезапускает юзербота")
else:
    add_module("restart", __file__)
    add_command("restart", f"{prefix}restart", "restarts the userbot")
