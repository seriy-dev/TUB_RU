import time
import os
import sqlite3
import info

conn = sqlite3.connect('database.sqlite')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS keys (
        service TEXT,
        key TEXT
    )
''')

services = ['aws_text']

for service in services:
    c.execute("SELECT service FROM keys WHERE service =?", (service,))
    row = c.fetchone()
    if not row:
        c.execute("INSERT INTO keys (service) VALUES (?)", (service,))
c.execute("SELECT service FROM keys WHERE service =?", ("prefix",))
row = c.fetchone()
if not row:
    c.execute("INSERT OR IGNORE INTO keys (service, key) VALUES (?, ?)", ("prefix", "!"))
c.execute("SELECT service FROM keys WHERE service =?", ("aws_status",))
row1 = c.fetchone()
if not row1:
    c.execute("INSERT OR IGNORE INTO keys (service, key) VALUES (?, ?)", ("aws_status", "off"))
conn.commit()


def cc():
    os.system('cls' if os.name == 'nt' else 'clear')


requirements = [
    "pip",
    "termcolor",
    "pyrogram",
    "TgCrypto",
    "requests",
    "gTTS",
    "apscheduler",
    "colorama",
    "psutil"
]


def download_requirements():
    cc()
    print('Пожалуйста подождите // Please wait...')
    import subprocess
    subprocess.run(['pip', 'install', 'tqdm', '-U', '-q'], check=True)
    from tqdm import tqdm
    cc()
    libraries = subprocess.run(["pip", "list"], check=True, capture_output=True, text=True).stdout
    for lib in tqdm(requirements, desc="Installing libraries..."):
        if lib not in libraries:
            subprocess.run(['pip', 'install', lib, '-U', '-q'], check=True)
        else:
            pass
    cc()


def update_userbot():
    import requests
    from tqdm import tqdm
    import time
    import info

    print("Поиск обновлений... // Searching for updates...")

    ver = requests.get("https://raw.githubusercontent.com/Timka4959000/TimkaUserBot/main/info.py").text
    ver = ver.split('version = "')[1].split('"')[0]

    if ver <= info.version:
        print("Обновления не найдены // No updates found")
        time.sleep(3)
        return
    else:
        print("Найдена новая версия! // New version found!")
        plugins_files = [
            "bot.py", "change_prefix.py", "help.py", "modules_actions.py",
            "ping.py", "restart.py", "send_log.py", "logo.py"
        ]

        for plugin in tqdm(plugins_files, desc="Обновление плагинов... // Updating plugins..."):
            new_code = requests.get(
                f"https://raw.githubusercontent.com/Timka4959000/TimkaUserBot/main/plugins/{plugin}"
            ).text
            new_code = new_code.replace('\r\n', '\n')
            plugin_path = f"plugins/{plugin}"

            with open(plugin_path, "w", encoding="utf-8") as file:
                file.write(new_code)

        system_files = [
            "main.py", "info.py", "helps/get_prefix.py", "helps/modules.py", "helps/scripts.py"
        ]

        for file in tqdm(system_files, desc="Обновление системы... // Updating system..."):
            new_code = requests.get(f"https://raw.githubusercontent.com/Timka4959000/TimkaUserBot/main/{file}").text
            new_code = new_code.replace('\r\n', '\n')

            with open(file, "w", encoding="utf-8") as old_file:
                old_file.write(new_code)

        print("Обновление успешно! // Update successful!")
        time.sleep(3)


def logging_setup():
    import logging

    logging.basicConfig(level=logging.INFO, filename="log.log", filemode="a+")


def login_client():
    cc()
    from pyrogram import Client, idle
    from pyrogram.enums import ParseMode
    from helps.scripts import get_lang

    if not os.path.isfile("restart.txt"):
        if os.path.isfile("TimkaUserBot.session-journal"):
            os.remove("TimkaUserBot.session-journal")

    if not os.path.isfile("lang.txt"):
        while True:
            lang_code = input("Select language // Выберите язык (ru/en): ")
            if lang_code not in ['en', 'ru']:
                cc()
                print("incorrect answer // некоректный ответ")
                time.sleep(3)
                cc()
            else:
                write_lang = open("lang.txt", "w")
                write_lang.write(lang_code)
                write_lang.close()
                break
    else:
        lang_code = get_lang()

    if not os.path.isfile("TimkaUserBot.session"):
        if lang_code == 'ru':
            api_id = input("Введите API ID: ")
            api_hash = input("Введите API Hash: ")
        else:
            api_id = input("Enter API ID: ")
            api_hash = input("Enter API Hash: ")

        app = Client(
            name="TimkaUserBot",
            api_hash=api_hash,
            api_id=api_id,
            device_model="POCO X3 PRO",
            system_version="ANDROID 13",
            app_version="10.2.9",
            lang_code=lang_code,
            plugins=dict(root="plugins"),
            parse_mode=ParseMode.HTML
        )
    else:
        app = Client(
            name="TimkaUserBot",
            plugins=dict(root="plugins")
        )

    with app:
        if not os.path.isfile("restart.txt"):
            pass
        else:
            f = open("restart.txt", "r")
            chat_id = f.read()
            f.close()

            os.remove("restart.txt")

            try:
                if lang_code == "en":
                    app.send_message(chat_id, "<b>TimkaUserBot successfully rebooted</b>")
                else:
                    app.send_message(chat_id, "<b>TimkaUserBot успешно перезагружен</b>")
            except Exception as e:
                if lang_code == "en":
                    app.send_message("me", f"<b>TimkaUserBot rebooted successfully, but an error occurred while "
                                           f"sending a message\n\nLOG:</b> {e}")
                else:
                    app.send_message("me", f"<b>TimkaUserBot успешно перезагружен, но произошла ошибка при отправке "
                                           f"сообщения\n\nLOG:</b> {e}")

    app.start()
    idle()
    app.stop()


if __name__ == "__main__":
    if not os.path.isfile("restart.txt"):
        download_requirements()
        update_userbot()
    logging_setup()
    login_client()
