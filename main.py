import time
import pip
import os
import sqlite3

conn = sqlite3.connect('database.sqlite')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS keys (
        service TEXT,
        key TEXT
    )
''')

services = ['gchat', 'gpt', 'aws_text']

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
    "pycryptodome",
    "termcolor",
    "pyrogram",
    "TgCrypto",
    "requests",
    "gTTS",
    "apscheduler",
    "nekobin",
    "art",
    "colorama"
  ]

def download_requirements():
    print('Подождите пожалуйста...')
    import subprocess
    subprocess.run(['pip', 'install', 'tqdm', '-U', '-q'], check=True)
    from tqdm import tqdm
    cc()
    libraries = subprocess.run(["pip", "list"], check=True, capture_output=True, text=True).stdout
    for lib in tqdm(requirements, desc="Установка библиотек..."):
        if lib not in libraries:
            subprocess.run(['pip', 'install', lib, '-U', '-q'], check=True)
        else:
            pass
    cc()

def logging_setup():
    import logging

    logging.basicConfig(level=logging.INFO, filename="log.log", filemode="a+")

def login_client():
    from pyrogram import Client, idle
    from pyrogram.enums import ParseMode

    if not os.path.isfile("restart.txt"):
        if os.path.isfile("TimkaUserBot.session-journal"):
            os.remove("TimkaUserBot.session-journal")

    if not os.path.isfile("TimkaUserBot.session"):
        api_id = input("Введите API ID: ")
        api_hash = input("Введите API Hash: ")
        app = Client(
            "TimkaUserBot",
            api_hash=api_hash,
            api_id=api_id,
            device_model="POCOX3PRO",
            system_version="ANDROID 13",
            app_version="10.1.1 (39265)",
            lang_code="ru",
            plugins=dict(root="plugins"),
            parse_mode=ParseMode.HTML
        )
    else:
        app = Client(
            "TimkaUserBot",
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
                app.send_message(chat_id, "<b>TimkaUserBot успешно перезагружен<b>")
            except Exception as e:
                app.send_message("me", f"<b>TimkaUserBot успешно перезагружен, но произошла ошибка при отправке сообщения\n\nLOG:<b> {e}")

    app.start()
    idle()
    app.stop()


if __name__ == "__main__":
    if not os.path.isfile("restart.txt"):
        download_requirements()
    logging_setup()
    login_client()
