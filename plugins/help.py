from pyrogram import Client, filters
from helps.modules import add_module, add_command, modules, commands, get_file_by_module

from helps.get_prefix import get_prefix
prefix = get_prefix()

@Client.on_message(filters.command("help", prefixes=prefix) & filters.me)
async def show_help(client, message):
    args = message.text.replace(f"{prefix}help", "").split(" ")
    try:
        if args[1] in modules:
            module_commands = commands[args[1]]
            result = ""
            for command_name, help_command in module_commands.items():
                result = result + f"{command_name} - {help_command}\n"
            file = get_file_by_module(args[1])
            await message.edit(f"""
📔 Название модуля: {args[1]}
📁 Расположение модуля: {file}

• Команды модуля:

{result}
                """)
        else:
            await message.edit("Данный модуль не найден")
    except IndexError:
        all_modules = ""
        for module in modules:
            all_modules = all_modules + f"⟩⟩ <code>{module}</code>\n"
        await message.edit(f"""
<b>📔 Все модули
         TimkaUserBot:</b>
{all_modules}

ℹ Всего модулей: {len(modules)}
❗ Смотреть все команды модулей и подробное разъяснение: {prefix}help [модуль]
                """)
        return

add_module("help", __file__)
add_command("help", f"{prefix}help", "увидеть все модули")
add_command("help", f"{prefix}help [модуль]", "посмотреть описание модуля")