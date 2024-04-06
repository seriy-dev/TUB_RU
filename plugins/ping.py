from datetime import datetime
from pyroru import Client, filters
from helps.modules import add_module, add_command
from helps.scripts import get_lang
from helps.get_prefix import get_prefix

prefix = get_prefix()
lang = get_lang()


class Texts:
    @staticmethod
    def get_texts():
        return {"ping": {
            "ru": f"<i>Понг!</i>\n<b>🏓 Пинг равен ",
            "en": f"<i>Pong!</i>\n<b>🏓 Ping is equal "
        }
        }


@Client.on_message(filters.command("ping", prefixes=prefix) & filters.me)
async def ping(client, message):
    text_versions = Texts.get_texts()
    start_t = datetime.now()
    await message.edit("🏓")
    end_t = datetime.now()
    time_taken_s = (end_t - start_t).microseconds / 1000
    await message.edit(text_versions['ping'][lang] + f"{round(time_taken_s)}ms</b>")


if lang == "ru":
    add_module("ping", __file__)
    add_command("ping", f"{prefix}ping", "получить пинг юзербота")
else:
    add_module("ping", __file__)
    add_command("ping", f"{prefix}ping", "Get the ping of a userbot.")
