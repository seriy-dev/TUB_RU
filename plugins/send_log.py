from pyrogram import Client, filters
from helps.modules import add_module, add_command
from helps.scripts import get_lang
from helps.get_prefix import get_prefix

lang = get_lang()
prefix = get_prefix()

class Texts:
    @staticmethod
    def get_texts():
        return {"logs": {
            "ru": f"<b>Логи TimkaUserBot</b>",
            "en": f"<b>Logs TimkaUserBot</b>"
        },
            "error": {
                "ru": "Лог пустой!",
                "en": "The log is empty!"
            }
        }


@Client.on_message(filters.command("send_log", prefixes=prefix) & filters.me)
async def send_log(client, message):
    text_versions = Texts.get_texts()
    try:
        await client.send_document(
            chat_id=message.chat.id,
            document=open("log.log", "rb"),
            caption=text_versions["logs"][lang]
        )
        await message.delete()
    except:
        await message.edit(text_versions['error'][lang])


if lang == "ru":
    add_module("send_log", __file__)
    add_command("send_log", f"{prefix}send_log", "Отправляет файл с логами")
else:
    add_module("send_log", __file__)
    add_command("send_log", f"{prefix}send_log", "Sends a file with logs")
