from pyrogram import Client
from pyrogram import filters as vrn
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from TGAssistant import BOT_TOKEN, OWNER_ID, API_ID, API_HASH

import logging
import asyncio

assistant = Client(
  api_id = API_ID,
  api_hash = API_HASH,
  session_name = "MY_TG_ASSISTANT"
  
)

PM_START_TEXT = """
Hello {},
I am [this}(t.me/user?id={}) person's assistant.
Just send me any message and I will forward it to my boss
"""
START_BTN = Inline
