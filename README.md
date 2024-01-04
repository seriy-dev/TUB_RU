<b>Инструкции установки</b>

Установка через termux: <pre language="bash">pkg install git && git clone https://github.com/Timka4959000/TimkaUserBot.git && cd TimkaUserBot && sh termux_setup.sh</pre>
Последующие запуски через termux: <pre language="bash">cd TimkaUserBot && sh termux_start.sh</pre>
Windows: 
1. Установите зип файл юзербота
2. Распакуйте в любую папку
3. Откройте папку и запустите файл windows_start.bat

<b>Дополнительные модули [official]:</b>

<a href='https://github.com/Timka4959000/TimkaUserBotModules'>репозитор</a>

<a href='https://t.me/TimkaUserBotModules'>телеграм канал</a>

<b>Пример модуля:</b>
<pre language='python'>
from pyrogram import Client, filters
from helps.modules import add_module, add_command, modules

from get_prefix import get_prefix
prefix = get_prefix()

@Client.on_message(filters.command("команда", prefixes=prefix) & filters.me)
async def bot(client, message):
    await message.edit("Пример модуля TimkaUserBot")

add_module("название модуля", __file__)
add_command("название модуля", f"{prefix}команда", "Пример команды для юзербота")
</pre>
