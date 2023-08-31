import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "تعاال يامطووري @Mvhmed 🥺❤",

            
           
 
            
            

        ]


        


@app.on_message(command(["جاكو","چاكو","محمد خالد"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
