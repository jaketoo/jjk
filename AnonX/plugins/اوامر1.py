

import asyncio

import os
import time
import requests
from config import START_IMG_URL,  MUSIC_BOT_NAME
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

@app.on_message(
    command(["م1"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم اوامر الفتح والقفل في بوت {MUSIC_BOT_NAME} ميوزك\n
**قفل / تعطيل + الامر**

ايدي / صورتي

صور / زوجني

نداء / زخرفه

**فتح / تفعيل + الامر**

ايدي / صورتي

صور / زوجني

نداء / زخرفه
لتنصيب بوت مشابه تواصل معي فالخاص @Mvhmed
**""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★𓏺𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙⚡", url=f"https://t.me/Mvhmed"),                        
                 ],[
                InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
               ],
          ]
        ),
    )
