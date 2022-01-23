# Code By @PeterParkerspide

import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.new_chat_members)
async def join(client, message):
    new_member = message.new_chat_members[0]
    msg = await message.reply_video("https://telegra.ph/file/b24dc362daae24b98fb7c.mp4",
                caption = f"""
**🙌Hey {new_member.first_name},**
**[{message.chat.title}] || Movie Requesting Group** ലേക്ക് സ്വാഗതം
നിങ്ങൾക്ക് വേണ്ട സിനിമയുടെ പേരും വർഷവും കൃത്യമായി **[Google](https://google.com/) ൽ നിന്നും നോക്കി അയക്കുക Movie എന്ന വാക്ക് അയക്കേണ്ട 😄. നമ്മുടെ ഗ്രൂപ്പ് പരമാവതി ♻️Share And Support♻️ ചെയ്യുക.☺️**
""", parse_mode="md",
     reply_markup = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("🔰 Canneil 🔰", url="https://t.me/flimsupdate")
      ],
      [
        InlineKeyboardButton("♻️ Share Group ♻️", url="https://t.me/share/url?url=https://t.me/tomhollandmovies")
     ]]))

    await asyncio.sleep(50)
    await msg.delete()
