# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Haii.. {message.from_user.first_name} Aku adalah πone-heart musicπ\n
πππ ππππππ πππ πππππ ππππππππ π πππ ππ ππππππππππ ππππ : @boyfriendnice
πππππππ πππππ πππππππππππ πππ ππππππ πππ πππ πππππππππ ππ π ππππ πππππππ πππππ πππππππ π ππππ ππππ ππππππππ ππππππ ππππππ.
βββββββββββββββ
β£ > πΉπ°π½πΆπ°π½ π»πΈππ π»π°πΆπ ππ΄πΊπ°π»πΈπΆππ ππ°πΊππ π΄ππΎπ.
β£ > πΉπΈπΊπ° π·π°π±πΈπ π³πΈπΌπ°ππΈπΊπ°π½ πΏπ°πΊππ° πΉπ°π½πΆπ°π½ 
    π»π°π½πΆπππ½πΆ πΏπ»π°π π»π°πΆπ πππ½πΆπΆπ ππ΄π±π΄π½ππ°π 
    πΉπΈπΊπ° ππΈπ³π°πΊ, π°ππΈπππ΄π½ ππΈπ³π°πΊ π°πΊπ°π½ π½π°πΈπΊ.
βββββββββββββββ
π€΅ππ»π?πͺπ½π?π­ π«π : [loveMe](https://t.me/boyfriendnice)
βοΈπ£π±πͺπ·π΄πΌ π―πΈπ» : [Grup Support](https://t.me/remaja_virtual62)
ββββββββββββββ
πππ πππππ : @vrtualsongbot - πππππππππ πππππ : @AsisstantMusic
 
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/boyfriendnice")
                  ],[
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/chvirtual62"
                    ),
                    InlineKeyboardButton(
                        "Group", url="https://t.me/remaja_virtual62") 
                  ],[
                    InlineKeyboardButton(
                        "Instagram", https://www.instagram.com/ikyyy_35"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aku sudah online, ayo kita joget ceria! πΆ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/boyfriendnice"
                    )
                ],[
                    InlineKeyboardButton(
                        "β Yes!", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "β No!", callback_data="close"
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
                        "π¦ Cara Memakai Bot Music!", url="https://t.me/humangabutguys/91577"
                    )
                ]
            ]
        ),
    )
