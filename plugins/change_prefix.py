from pyrogram import Client, filters
from helps.modules import add_module, add_command
from helps.scripts import set_key, restart

from helps.get_prefix import get_prefix
prefix = get_prefix()

@Client.on_message(filters.command("cp", prefixes=prefix) & filters.me)
async def change_prefix(client, message):
    try:
        new_prefix = message.text.split()[1]
    except IndexError:
        await message.reply_text(
            "Вы неправильно используете команду! Помощь - !help changeprefix"
        )
        return
    await set_key("prefix", new_prefix)
    await message.edit(
        f"Новый префикс: [{message.text.split()[1]}]"
    )
    await message.reply("<b>Перезагружаю юзербота...</b>")
    await restart(message=message.chat.id)

add_module("changeprefix", __file__)
add_command("cp", f"{prefix}changeprefix [префикс]", "меняет префикс")