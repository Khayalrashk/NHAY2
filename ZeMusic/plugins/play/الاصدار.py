import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["الاصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/57036e277059ef8608dd3.jpg",
        caption=f"""**اهلا بك عزيزي {message.from_user.mention} في اصدار سورس لاريـن
★᚜ اسم سورس : لاريـن
★᚜ نوع : ميـوزك

★᚜ اللغه : اللغه العربيه ويدعم الانجليزيه 

★᚜ مجال العمل : بوتات تشغيل الموسيقى في الاتصال
★᚜ نظام التشغيل : كارولين بوت ميوزك
★᚜ الاصدار 2.0.14
★᚜ تاريخ التأسيس : 2024/6/1

★᚜ مؤسس  سورس لاريـن : [• 𝐊𝐡𝐚𝐲𝐚𝐥 𓏺](https://t.me/F_A_6)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒𝐨𝐮𝐫𝐜𝐞 𝐥𝐨𝐥 🧚‍♀", url=f"https://t.me/K55DD"), 
                 ],[
                 InlineKeyboardButton(
                        "", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )

