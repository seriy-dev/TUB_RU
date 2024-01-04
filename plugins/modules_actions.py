from pyrogram import Client, filters
from helps.modules import add_module, add_command, load_module, modules
import os

from helps.get_prefix import get_prefix
from helps.scripts import restart

prefix = get_prefix()


@Client.on_message(filters.command(["lmodule", "load_module", "lm"], prefix) & filters.me)
async def lmodule(client, message):
    if not message.reply_to_message:
        try:
            link = message.command[1]
        except:
            await message.edit(f"Помощь: {prefix}help load_module")
            return
        info = load_module(link)
        if os.path.isfile(f"plugins/{info[0]}"):
            await message.edit("Файл с названием как у этого модуля уже существует!")
            return

        f = open(f"plugins/{info[0]}.py", "w+")
        f.write(info[1])
        f.close()

        await message.edit(f"{info[0].replace('.py', '')} успешно установлен!")
        await message.reply("<b>Перезагружаю юзербота...</b>")
        await restart(message=message)

    else:

        await client.download_media(message.reply_to_message.document, file_name='plugins/')
        await message.edit("Модуль успешно установлен!")
        await message.reply("<b>Перезагружаю юзербота...</b>")
        await restart(message=message)


add_module("load_module", __file__)
add_command("load_module", f"{prefix}load_module [raw ссылка/в ответ на файл с модулем]", "устанавливает модуль")
add_command("lmodule", f"{prefix}load_module [raw ссылка/в ответ на файл с модулем]", "устанавливает модуль")
add_command("lm", f"{prefix}load_module [raw ссылка/в ответ на файл с модулем]", "устанавливает модуль")
