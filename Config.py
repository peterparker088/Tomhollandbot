import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot Settings
SESSION = environ.get('SESSION', 'LuciferMoringstar_Robot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
BOT_USERNAME = environ.get('BOT_USERNAME', 'LuciferMoringstar_Robot')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

BROADCAST_CHANNEL = int(os.environ.get("BROADCAST_CHANNEL", ""))
ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "").split())
DB_URL = os.environ.get("DATABASE_1", "")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

# Photo Mode
PICS = (environ.get('PICS', 'https://telegra.ph/file/497f21338351cef6cc1fd.jpg https://telegra.ph/file/60ec3a4a522d06b5e4a2c.jpg https://telegra.ph/file/90345e9255d32f5c8ad75.jpg https://telegra.ph/file/e81e25e0c3ee753530c7f.jpg https://telegra.ph/file/41aaa2bc85bad6986641b.jpg https://telegra.ph/file/78f1bd0309d6607dc44fa.jpg https://telegra.ph/file/4e0bbf59af8c55dfce9ff.jpg https://telegra.ph/file/7ae43915facd8eb0a3d00.jpg https://telegra.ph/file/2e91f2168859795bebec1.jpg https://telegra.ph/file/2c91985dd562ea835ef3b.jpg https://telegra.ph/file/daab7f2becc4ddab45586.jpg https://telegra.ph/file/7beda83fbe243952f6768.jpg https://telegra.ph/file/c3fdb36e73269c2e4d629.jpg https://telegra.ph/file/07af4bdb370593909aa51.jpg')).split()
SEPLLING_MODE_PICS = (environ.get('SEPLLING_MODE_PICS', 'https://telegra.ph/file/7658da66b1771aabd026c.mp4 https://telegra.ph/file/90345e9255d32f5c8ad75.jpg https://telegra.ph/file/e81e25e0c3ee753530c7f.jpg https://telegra.ph/file/41aaa2bc85bad6986641b.jpg https://telegra.ph/file/78f1bd0309d6607dc44fa.jpg https://telegra.ph/f https://telegra.ph/file/7658da66b1771aabd026c.mp4 https://telegra.ph/file/7658da66b1771aabd026c.mp4 https://telegra.ph/file/7658da66b1771aabd026c.mp4 https://telegra.ph/file/7658da66b1771aabd026c.mp4 https://telegra.ph/file/7658da66b1771aabd026c.mp4 https://telegra.ph/file/7658da66b1771aabd026c.mp4 https://telegra.ph/file/7658da66b1771aabd026c.mp4')).split()

# Seplling Mode
SEPLLING_MODE_TEXT = environ.get("SEPLLING_
# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('FORCES_SUB')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
TUTORIAL = "https://youtu.be/5hnYOKBzyi8"
# MongoDB information
DATABASE_URI = environ['DATABASE_2']
DATABASE_NAME = environ['BOT_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Auto Filter V3**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)
START_IMG = environ.get("START_IMG", "")

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
