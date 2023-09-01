from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from config import SUPPORT_CHANNEL



def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الي مجموعتك او قناتك ⚡",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="الأوامر",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الي مجموعتك او قناتك ⚡",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="الأوامر", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="لتنصيب بوت", url=f"https://t.me/Mvhmed"
            ),
            InlineKeyboardButton(
                text="👤 مطور البوت", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="قناة المطور", url=f"https://t.me/{SUPPORT_CHANNEL}"
            )
        ],
      
     ]
    return buttons
