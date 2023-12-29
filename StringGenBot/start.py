from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝐇𝐞𝐲 {msg.from_user.mention}🍷,

ɪ ᴀᴍ  {me2},
ᴛʀᴜsᴛᴇᴅ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.
ғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ.
ɴᴏ ᴀɴʏ ᴇʀʀᴏʀ.

ᴍᴀᴅᴇ ʙʏ   : [ᴘᴍ ʙᴏᴛ](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⚡ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ⚡", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("✨ sᴜᴘᴘᴏʀᴛ ✨", url="https://t.me/FRIENDS2FAMILY_0"),
                    InlineKeyboardButton("🥀 ᴜᴘᴅᴀᴛᴇ 🥀", url="https://t.me/The_F2F_Shayri")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
