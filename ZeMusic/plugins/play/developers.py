import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(command(["المبرمج","مبرمج","مبرمج السورس","مطور السورس","خيال"]))
async def devid(client: Client, message: Message):
    usr = await client.get_chat(5901732027)
    name = usr.first_name
    usrnam = usr.username
    uid = 5901732027
    bio = usr.bio
    await app.download_media(usr.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
       
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"""<b>-› 𝙽𝙰𝙼𝙴 ¦ :{name}\n -› 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 ¦ :@{usrnam}\n -› 𝙸𝙳 ¦ :`{uid}`\n -› 𝙱𝙸𝙾 ¦ :{bio}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         name, url=f"https://t.me/{usrnam}"), 
                 ],[
                   InlineKeyboardButton(
                        "• 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐚𝐫𝐢𝐧 ♩", url=f"https://t.me/SOURCELARIN"),
                ],

            ]

        ),

    )
