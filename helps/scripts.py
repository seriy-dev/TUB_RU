import nekobin
from main import c, conn, cc
import logging, sys, os
from nekobin import NekoBin, errors
from pyrogram import Client


async def restart(message):
    f = open("restart.txt", "w")
    if message.chat.username:
        f.write(str(message.chat.username))
    else:
        f.write(str(message))
    f.close()
    os.execvp(sys.executable, [sys.executable, *sys.argv])


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


async def neko(text: str):
    try:
        neko = await nekobin.nekofy(
            content=text,
            title="code",
            author="TimkaUserBot"
        )
    except errors.HostDownError:
        return "Host is down at the moment!"
    except:
        return "Pasting failed!"
    return neko.url
