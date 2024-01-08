import os
import subprocess
from pyrogram import Client, filters, __version__
import platform
from platform import python_version
from info import version
from helps.modules import add_module, add_command, modules
from helps.get_prefix import get_prefix
from helps.scripts import get_lang

lang = get_lang()
prefix = get_prefix()


class Texts:
    @staticmethod
    def get_texts(me, system, prefix):
        return {"info": {
            "ru": f"""
<b><emoji id='4999015678238262018'>✨</emoji> | TimkaUserBot  
👤 | Владелец: {me.mention}
📁 | Кол-во модулей: {len(modules)}
💻 | Система: {system}
❗ | Префикс: {prefix}
🤖 | Версия юзербота: {version}
🐍 | Python: {python_version()}
🥧 | Pyrogram: {__version__}
👑 | Юзербот создан @fimkov</b>
            """,
            "en": f"""
<b><emoji id='4999015678238262018'>✨</emoji> | TimkaUserBot  
👤 | Owner: {me.mention}
📁 | Number of modules: {len(modules)}
💻 | System: {system}
❗ | Prefix: {prefix}
🤖 | Userbot version: {version}
🐍 | Python: {python_version()}
🥧 | Pyrogram: {__version__}
👑 | Userbot by @fimkov</b>
            """
        }
        }


@Client.on_message(filters.command("bot", prefixes=prefix) & filters.me)
async def bot(client, message):
    termux_execution = "PREFIX" in os.environ
    if termux_execution:
        android_version_process = subprocess.run(['getprop', 'ro.build.version.release'], capture_output=True,
                                                 text=True)
        android_version = android_version_process.stdout.strip()
        system = f"Termux [Android {android_version}]"
    else:
        system = platform.system()

    me = await client.get_me()
    text_versions = Texts.get_texts(me, system, prefix)

    try:
        await client.send_photo(chat_id=message.chat.id, photo='logo.png', caption=text_versions["info"][lang])
        await message.delete()
    except:
        await message.edit(text_versions["info"][lang])


if lang == "ru":
    add_module("userbot_info", __file__)
    add_command("userbot_info", f"{prefix}bot", "Получить информацию о юзерботе")
else:
    add_module("userbot_info", __file__)
    add_command("userbot_info", f"{prefix}bot", "Get information about the userbot")
