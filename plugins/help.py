from pyrogram import Client, filters
from helps.modules import add_module, add_command, modules, commands, get_file_by_module
from helps.scripts import get_lang
from helps.get_prefix import get_prefix

lang = get_lang()
prefix = get_prefix()

class Texts:
    @staticmethod
    def get_texts(name=None, file=None, commands=None, all_modules=None):
        return {"error": {
            "ru": f"Данный модуль не найден",
            "en": f"This module was not found"
        },
            "module": {
                "ru": f"""
📔 Название модуля: <code>{name}</code>
📁 Расположение модуля: <code>{file}</code>

• Команды модуля:
<i>{commands}</i>
                """,
                "en": f"""
📔 Module name: <code>{name}</code>
📁 Module location: <code>{file}</code>

• Module commands:
<i>{commands}</i>
                """
            },
            "modules": {
                "ru": f"""
<b>📔 Все модули
         TimkaUserBot:</b>
{all_modules}

ℹ Всего модулей: {len(modules)}
❗ Для получении информации о модуле: {prefix}help [модуль]
                """,
                "en": f"""
<b>📔 All modules
         TimkaUserBot:</b>
{all_modules}

ℹ Total modules: {len(modules)}
❗ To get information about the module: {prefix}help [module]
                """
            }
        }

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
            text_versions = Texts.get_texts(name=message.command[1], file=file, commands=result)
            await message.edit(text_versions['module'][lang])
        else:
            text_versions = Texts.get_texts()
            await message.edit(text_versions['error'][lang])
    except IndexError:
        all_modules = ""
        for module in modules:
            all_modules = all_modules + f"⟩⟩ <code>{module}</code>\n"
        text_versions = Texts.get_texts(all_modules=all_modules)
        await message.edit(text_versions['modules'][lang])
        return

if lang == "ru":
    add_module("help", __file__)
    add_command("help", f"{prefix}help", "Просмотреть все модули")
    add_command("help", f"{prefix}help [имя модуля]", "Посмотреть описание модуля и команды")
else:
    add_module("help", __file__)
    add_command("help", f"{prefix}help", "View all modules")
    add_command("help", f"{prefix}help [module name]", "View module description and commands")
