from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from ZeMusic import app

channel = "eo_u7"
command_list = ("تشغيل", "بحث", "تخطي", "استئناف", "تقديم", "تحميل", "توقف", "مؤقت", "كمل", "كملي", "لارين بحث", "غنيلي", "شعر", "قران", "اذكار", "ادعيه", "play", "شغلي", "شغل", "vplay", "vتشغيل", "cplay", "cvplay", "playforce", "vplayforce", "cplayforce", "cvplayforce", "start", "stats", "الاوامر", "اوامر", "ميوزك", "بنج", "سرعه", "song", "/song", "/start")

async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: await app.get_chat_member(channel, user_id)
    except UserNotParticipant: return False
    return True

subscribed = filters.create(subscription)

@app.on_message(~subscribed & filters.command(command_list))
async def checker(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]: await message.delete()
    user_id = message.from_user.id
    user = message.from_user.first_name
    markup = Markup([
        [Button("اضغط للاشتراك", url=f"https://t.me/{channel}")]
    ])
    await message.reply(
        f"❥ عذراً عزيزي {user}/n ❥ عليك الإشتراك في القناة اولاً ☜ @eo_u7",
        reply_markup = markup
    )
