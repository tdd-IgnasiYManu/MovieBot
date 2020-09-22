#!/usr/bin/env python
import os
import pathlib as pl
from pyrogram import Client, filters
from dotenv import load_dotenv

env_path = pl.Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

API_HASH = os.getenv('API_HASH')
API_ID = os.getenv('API_ID')

app = Client("pyrogram_bot", api_id=API_ID, api_hash=API_HASH)


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f'Hola {message.from_user.mention}')


app.run()
