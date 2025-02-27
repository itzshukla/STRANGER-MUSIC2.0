    import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("24753274"))
API_HASH = getenv("625668050f7e193a994e2f5ddc4aafe5")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7743484569:AAFqAjXFHBG6bAeN0XooVYkofHd-UYO-UZE")

# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "@Infinity_powerfull_bot")

# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "˹ 𝗦ᴀᴘɴᴀ ✘ 𝗠ᴜsɪᴄ ˼")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://gxinfinity742:gxinfinity742@cluster0.4crk9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002273083150"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("7290350162"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

    # Don't edit variables below this line #
SUDO_USERS = [7290350162 , 7135072912 ]

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/itzshukla/STRANGER-MUSIC2.0",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/gxinfinity_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT","https://t.me/infinitygx_bot_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @VIP_STRING_ROBOT on Telegram
STRING1 = getenv("BQF5tHoAYm8U3zWai-PzIw_NfhaJxMp3YphU2Hrs9cYwwoufmaLkc_Fb_f2ZBSJHL7ogb7ImdYpUQ54poeiiUQXPLSCjONR0rJat1AgoMerJG6EciagkY0BuOadKb2Ns3_Qg-6YQkp3EqB75BtAlbRNCBrymRPJNXzxp2pJ5bLmqIaNVHuHX9vAXYKjbzNJNR1SenVFwTL9cdAwEIXqTelMDZFI3u16T5-AeiMDy_27R0KJ_1Bv5YYSYOGjVBIrZPGC5nnm5evi2hURqxzHjL-eqs0eBXv3cRFb6AGxtE_m52Hh1XhVT1rqQrIRlCxfuTngbeOsSHUqCC5_9VJfJMTO_tT5LJwAAAAHNjDKZAQ", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

###############################

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/0b637v.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/80e35d93784e239bdc86c.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
