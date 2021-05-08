from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Haii Guys, Apa Kabar Kamu??:)) {message.from_user.first_name}!</b>

𝐀𝐊𝐔 𝐀𝐃𝐀𝐋𝐀𝐇 𝐁𝐎𝐓 𝐌𝐔𝐒𝐈𝐊 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐘𝐀𝐍𝐆 𝐃𝐈 𝐊𝐄𝐌𝐁𝐀𝐍𝐆𝐊𝐀𝐍 𝐎𝐋𝐄𝐇 : @boyfriendnice
𝐀𝐏𝐀𝐁𝐈𝐋𝐀 𝐈𝐍𝐆𝐈𝐍 𝐌𝐄𝐍𝐆𝐆𝐔𝐍𝐀𝐊𝐀𝐍 𝐀𝐊𝐔 𝐈𝐍𝐕𝐈𝐓𝐄 𝐀𝐊𝐔 𝐃𝐀𝐍 𝐀𝐒𝐈𝐒𝐒𝐓𝐀𝐍𝐓 𝐍𝐘𝐀 𝐀𝐆𝐀𝐑 𝐁𝐈𝐒𝐀 𝐁𝐄𝐑𝐉𝐀𝐋𝐀𝐍 𝐃𝐄𝐍𝐆𝐀𝐍 𝐋𝐀𝐍𝐂𝐀𝐑 𝐉𝐀𝐃𝐈𝐊𝐀𝐍 𝐀𝐃𝐌𝐈𝐍 𝐊𝐄𝐃𝐔𝐀𝐍𝐘𝐀.
════════════════════════════
│>𝙹𝙰𝙽𝙶𝙰𝙽 𝙻𝙸𝚂𝚃 𝙻𝙰𝙶𝚄 𝚂𝙴𝙺𝙰𝙻𝙸𝙶𝚄𝚂 𝚃𝙰𝙺𝚄𝚃 𝙴𝚁𝙾𝚁.
│>𝙹𝙸𝙺𝙰 𝙷𝙰𝙱𝙸𝚂 𝙳𝙸𝙼𝙰𝚃𝙸𝙺𝙰𝙽 𝙿𝙰𝙺𝚂𝙰 𝙹𝙰𝙽𝙶𝙰𝙽 
│𝙻𝙰𝙽𝙶𝚂𝚄𝙽𝙶 𝙿𝙻𝙰𝚈 𝙻𝙰𝙶𝚄 𝚃𝚄𝙽𝙶𝙶𝚄 𝚂𝙴𝙱𝙴𝙽𝚃𝙰𝚁 𝙹𝙸𝙺𝙰 
│𝚃𝙸𝙳𝙰𝙺, 𝙰𝚂𝙸𝚂𝚃𝙴𝙽 𝚃𝙸𝙳𝙰𝙺 𝙰𝙺𝙰𝙽 𝙽𝙰𝙸𝙺.
════════════════════════════
𝐉𝐈𝐊𝐀 𝐀𝐃𝐀 𝐊𝐄𝐍𝐃𝐀𝐋𝐀 𝐁𝐈𝐒𝐀 𝐂𝐇𝐀𝐓 𝐎𝐖𝐍𝐄𝐑𝐍𝐘𝐀!!
════════════════════════════
𝐁𝐎𝐓 𝐌𝐔𝐒𝐈𝐊 : @officialheartbot 
𝐀𝐒𝐈𝐒𝐒𝐓𝐀𝐍𝐓 𝐌𝐔𝐒𝐈𝐊 : @AsisstantOneHeart


        """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "⚡ Owner", url="https://t.me/boyfriendnice")
                  ],[
                    InlineKeyboardButton(
                        "🍃 Channel Aku", url="https://t.me/chvirtual62"
                    ),
                    InlineKeyboardButton(
                        "❤️ Grup", url="https://t.me/remaja_virtual62") 
                  ],[
                    InlineKeyboardButton(
                        "👸 My bot help", url="https://t.me/@Asisstant_groupbot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**💕 Pemutar Musik Is The On!**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌙 Group Support", url="https://t.me/remaja_virtual62"
                    ),
                    InlineKeyboardButton(
                        "⚡ Owner", url="https://t.me/boyfriendnice"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🎧 Pemutar Musik Is The On!**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ Onwer", url="https://t.me/boyfriendnice") 
                ],[
                    InlineKeyboardButton(
                        "🌙 Group Support", url="https://t.me/remaja_virtual62"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Klik tombol dibawah untuk melihat panduan menggunakan bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦇 Cara Memakai Bot Music!", url="https://t.me/humangabutguys/91577"
                    )
                ]
            ]
        ),
    )
