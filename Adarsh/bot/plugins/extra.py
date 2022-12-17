from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from Adarsh import StartTime


START_TEXT = """ Your Telegram DC Is : `{}`  """


@StreamBot.on_message(filters.regex("maintainers😎"))
async def maintainers(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="Radhe Radhe ❤️",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡 ❤️ 𝐁𝐲  [ᗪᥙɗᥙ ᥫ᭡ ](https://t.me/Bae_wafaaa)",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🍥 Contact 🍥 ", url=f"https://t.me/Bae_wafaaa")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
            
         
@StreamBot.on_message(filters.regex("follow❤️"))
async def follow_user(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="Radhe Radhe ❤️",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<B>Here's [⚡️AK IMAX HUB⚡️](https://t.me/akimaxmovies)</B>",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("⚡️AK IMAX HUB⚡️", url=f"https://t.me/akimaxmovies")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
        

@StreamBot.on_message(filters.regex("DC"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True
    )

    
    
@StreamBot.on_message(filters.command("list"))
async def list(l, m):
    LIST_MSG = "Hi! {} Here is a list of all my commands \n \n 1 . `start⚡️` \n 2. `help📚` \n 3. `login🔑` \n 4.`follow❤️` \n 5. `ping📡` \n 6. `status📊` \n 7. `DC` this tells your telegram dc \n 8. `maintainers😎` "
    await l.send_message(chat_id = m.chat.id,
        text = LIST_MSG.format(m.from_user.mention(style="md"))
        
    )
    
    
@StreamBot.on_message(filters.regex("ping📡"))
async def ping(b, m):
    start_t = time.time()
    ag = await m.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await ag.edit(f"⚡️Pong!!!\n{time_taken_s:.3f} ms")
    
    
    
    
@StreamBot.on_message(filters.private & filters.regex("status📊"))
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = f'<b>╭──「⭕️ BOT STATISTICS ⭕️」</b>\n' \
             f'<b>│</b>\n' \
             f'<b>├ ⚡️ AK-IMAX | FILE TO LINK BOT ⚡️</b>\n' \
             f'<b>├  🆚 Version : 1.0</b>\n' \
             f'<b>├  ⌚️Bot Uptime :</b> {currentTime}\n' \
             f'<b>│</b>\n' \
             f'<b>Bot Uptime :</b>\n' \
             f'<b>├  🗃 Total Disk Space :</b> {total}\n' \
             f'<b>├  📀 Total Used Space :</b> {used}\n' \
             f'<b>│</b>\n' \
             f'<b>├ 📊Data Usage📊</b>\n' \
             f'<b>├  🔼 Total Upload : </b> {sent}\n' \
             f'<b>├  🔽 Total Download : </b> {recv}\n' \
             f'<b>│</b>\n' \
             f'<b>├  🗄 CPU :</b> {cpuUsage}% ' \
             f'<b>├  🎮 RAM :</b> {memory}% ' \
             f'<b>├  💽 DISK : </b> {disk}%' \
             f'<b>│</b>\n' \
             f'<b>╰──「 🚸 [⚡️Ak-imax⚡️ ](https://t.me/akimaxmovies) 🚸 」'
  await update.reply_text(botstats)
