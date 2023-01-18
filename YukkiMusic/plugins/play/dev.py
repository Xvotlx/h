import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

@app.on_message(
    command(["المطور"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f6d4da3bdfc12b40291f7.jpg",
       caption=f"""❲#baran
𓏺 𓏺 𝖲𝖮𝖴𝖱𝖢𝖤 𝖡𝖠𝖱𝖮 🐉 .
👨🏼‍💻 يوزر المطور : @z_2_z """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◍:👮🏼‍♂️ مالك البوت √", url=f"https://t.me/z_2_z")
                ],[
                    InlineKeyboardButton(
                        "اضف البوت الي مجموعتك✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
    )