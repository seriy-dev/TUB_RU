import os
import subprocess
from pyrogram import Client, filters, __version__
import platform
from platform import python_version
from info import version
from helps.modules import add_module, add_command, modules

from helps.get_prefix import get_prefix
prefix = get_prefix()

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
    try:
        await client.send_photo(chat_id=message.chat.id, photo='logo.png', caption=f"""
<b><emoji id='4999015678238262018'>✨</emoji> | TimkaUserBot  
👤 | Владелец: {me.mention}
📁 | Кол-во модулей: {len(modules)}
💻 | Система: {system}
❗ | Префикс: {prefix}
🤖 | Версия юзербота: {version}
🐍 | Python: {python_version()}
🥧 | Pyrogram: {__version__}</b>
👑 | создатель юзербота: @fimkov
    """)
        await message.delete()
    except:
        await message.edit(f"""
<b><emoji id='4999015678238262018'>✨</emoji> | TimkaUserBot
👤 | Владелец: {me.mention}
📁 | Кол-во модулей: {len(modules)}
💻 | Система: {system}
❗ | Префикс: {prefix}
🤖 | Версия юзербота: {version}
🐍 | Python: {python_version()}
🥧 | Pyrogram: {__version__}</b>
👑 | создатель юзербота: @dev_fimkov
    """)

add_module("userbot_info", __file__)
add_command("userbot_info", f"{prefix}bot", "Получить информацию о юзерботе")
