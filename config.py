#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7422740043:AAGF5b94e9fT6970U5RfOqSKmJXX0tULZ2g")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", " 29628312"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "09384c20a76a08fe4bdd8c3f4a0f2aaa")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", " -1002176036656"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1204461723"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://seriespeekbusiness:OoZAHoqKFAMVNq5V@cluster0.nwfwcj5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002198318434"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Yo {mention}, I'm Deadpool. I'm here to provide you the movie or series you requested.😉 /n /nI wish you a good day, Join & Share SeriesPeek (https://t.me/SeriesPeek) to make my day good.😁 /nThanks for the Support.😙</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1204461723").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Heyyy {mention}, I noticed that you haven't joined SeriesPeek (https://t.me/SeriesPeek) yet.🧐 /nDo you wanna die???😾🔪</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "{filename} /n•────•────────•────• /n📌 ᴅɪsᴄᴜssɪᴏɴ : ᴄʟɪᴄᴋ ʜᴇʀᴇ (https://t.me/SeriesPeekDiscussion) /n©️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : ᴄʟɪᴄᴋ ʜᴇʀᴇ (https://t.me/SeriesPeek) /n⚜️ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ : ᴄʟɪᴄᴋ ʜᴇʀᴇ (https://t.me/NeecheSeTopperr) /n•────•────────•────• /n🎗 ʝσιи • ѕнαяє • ѕυρρσят 🎗")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1204461723)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
