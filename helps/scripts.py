import nekobin
from main import c, conn
import logging, sys, os


async def restart(message=None):
    f = open("restart.txt", "w")
    if message:
        if message.chat.username:
            f.write(str(message.chat.username))
        else:
            f.write(str(message.chat.id))
    else:
        f.write("me")
    f.close()
    os.execvp(sys.executable, [sys.executable, *sys.argv])


def get_lang():
    lang_get = open("lang.txt", "r")
    lang = lang_get.read()
    lang_get.close()
    return lang


async def get_keys(keys_to_search: list) -> list:
    keys_found = []
    for key in keys_to_search:
        c.execute("SELECT key FROM keys WHERE service =?", (key,))
        row = c.fetchone()[0]
        keys_found.append(row)
    return keys_found


async def set_key(key_to_search: str, new_key: str):
    c.execute("SELECT key FROM keys WHERE service=?", (key_to_search,))
    row = c.fetchone()[0]
    if not row:
        logging.error(row)
    else:
        try:
            c.execute("UPDATE keys SET key=? WHERE service=?", (new_key, key_to_search))
            conn.commit()
            return True
        except Exception as e:
            logging.error(e)
    conn.commit()
