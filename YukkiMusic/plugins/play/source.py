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
    command(["سورس زيرو","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/da6801ca62f25c042f570.jpg",
        caption=f"""[WelCoMe To SoUrCe Baroo 🌐](https://t.me/z_2_7)\n\n[ThE BesT SoUrCe oN TelEGrAM 🌐](https://t.me/z_2_7)\n\n[ FoLLOw ThE BuTtOns BeLoW ⚡️](https://t.me/z_2_7)\n\n""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "›: 𓏺 َِ𝗕َِ!َِ𝗮َِ𝗿َِ𝗮َِ𝗻 ↜.", url=f"https://t.me/z_2_z"), 
                ],[
                    InlineKeyboardButton(
                        "›: َِ𓏺 َِ𝗠َِ!َِ𝗢َِ𝗗َِ𝗬↜.", url=f"https://t.me/y_v_2"), 
                ],[

                    InlineKeyboardButton(
                        "𓏺 𓏺 𝖲𝖮𝖴𝖱𝖢𝖤 𝖡𝖠𝖱𝖮 🐉 .", url=f"https://t.me/z_2_7"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك✅.", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],

            ]

        ),

    )