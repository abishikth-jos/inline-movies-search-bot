import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int("3264452") #int(environ['API_ID', 3264452])
API_HASH = "dfa13ad72701f1bbaba18eb59fd52df3" #environ['API_HASH', 'dfa13ad72701f1bbaba18eb59fd52df3']
BOT_TOKEN = "1682428637:AAFhIqMTMJIYpOGWTNgEEaYWv44aXmrw5nk" #environ['BOT_TOKEN', '1682428637:AAFhIqMTMJIYpOGWTNgEEaYWv44aXmrw5nk']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = int(1416381241) #[int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS', 1416381241].split()]
CHANNELS = int(-1001394559471) #[int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS','-1001394559471'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = "mongodb+srv://MediaSearch:MediaSearch@cluster0.51ylhch.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  #environ['DATABASE_URI', 'mongodb+srv://MediaSearch:MediaSearch@cluster0.51ylhch.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0']
DATABASE_NAME = "MediaSearch" #environ['DATABASE_NAME', 'MediaSearch' ]
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search Bot or ypu can call me as Auto-Filter Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

BUTTON = environ.get("BUTTON",False)
FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
