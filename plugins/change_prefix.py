from pyrogram import Client, filters
from helps.modules import add_module, add_command
from helps.scripts import set_key, restart
from helps.scripts import get_lang
from helps.get_prefix import get_prefix

lang = get_lang()
prefix = get_prefix()

class Texts:
    @staticmethod
    def get_texts(new_prefix):
        return {"error": {
            "ru": f"Вы неправильно используете команду! Помощь - {prefix}help changeprefix",
            "en": f"You are using the command incorrectly! Help - {prefix}help changeprefix"
        },
            "prefix": {
                "ru": f"Новый префикс: {new_prefix}",
                "en": f"New prefix: {new_prefix}"
            },
            "reload": {
                "ru": "<b>Перезагружаю юзербота...</b>",
                "en": "<b>Rebooting the userbot...</b>"
            }
        }

@Client.on_message(filters.command("cp", prefixes=prefix) & filters.me)
async def change_prefix(client, message):
    try:
        new_prefix = message.text.split()[1]
    except IndexError:
        text_versions = Texts.get_texts(new_prefix)
        await message.edit(text_versions["error"][lang])
        return

    text_versions = Texts.get_texts(new_prefix)

    await set_key("prefix", new_prefix)
    await message.edit(text_versions["prefix"[lang]])
    await message.reply(text_versions['reload'][lang])
    await restart(message=message)

if lang == "ru":
    add_module("changeprefix", __file__)
    add_command("changeprefix", f"{prefix}cp [префикс]", "меняет префикс")
else:
    add_module("changeprefix", __file__)
    add_command("changeprefix", f"{prefix}cp [prefix]", "changes prefix")
