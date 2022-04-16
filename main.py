# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/frankenstein-666/MegaDL-Bot>

import os
import asyncio
from config import Config
from pyrogram import Client, idle

if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="megadl")
    app = Client(
        "MegaDL-Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.start()
    print('\n\n>>> MegaDL-Bot Started. Join @project_3301!')
    idle()
    app.stop()
    print('\n\n>>> MegaDL-Bot Stopped. Join @projact_3301!')
