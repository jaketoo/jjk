import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("help")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3123f5336cb10b95f6c0d.jpg",
        caption=f"""** 𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس چــاکـو \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n** 𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙", url=f"https://t.me/Mvhmed"),
                    InlineKeyboardButton(
                        "الغشيم", url=f"https://t.me/Mvhmed"),
                ],[
                
                    InlineKeyboardButton(
                        "★ 𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙⚡", url=f"https://t.me/Mvhmed"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""** 𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦اكتب سؤال + سؤالك - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

** 𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="usage")],
            [InlineKeyboardButton("𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙", url=f"https://t.me/Mvhmed")
             
            [InlineKeyboardButton("★ الغشيم⚡", url=f"https://t.me/Mvhmed")],
        ]
    ))
