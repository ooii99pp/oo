## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAb6bxQLUeATxuB_FdPCER5PT8c8KqKS1EMiEV0GpqFz9WxRdMGOu16THgFLW2tqf6CN2QMdnYf2vyHw23o2LlCcRLjIONGEKfXbw4bFv_3AF3UCMEWoIWjW6ZG32IxINP9c-mHz1IxB3KypGwSbmrXO2Nw13e9HfHezmbosVJ13gWYZJ1lAS9-qicNePY3G_3wrjBaQQyrqtvjdTOODS5OhiZoQP6IBGnDyV1pUO1C6P8J6gM9yfqX823sXDESEviHVqb1qjDqV_TZRTGJka3tXWXzzQEVXohfj5b0If3ervBc5bsO48WcaYONtW9l6V0uAkS0l0iGr7jiXerB0-ecAAAAAUjjBCwA")
BOT_TOKEN = getenv("BOT_TOKEN", "5433958614:AAGV9mPpwzb-GJeNXhYmduWDni5AOLmmT0I")
BOT_NAME = getenv("BOT_NAME", "𝖬𝗎𝗌𝗂𝖼 .")
API_ID = int(getenv("API_ID", "12987601"))
API_HASH = getenv("API_HASH", "a6581bb9160931c45197461bb7e81f90")
OWNER_NAME = getenv("OWNER_NAME", "ABBAS")
OWNER_USERNAME = getenv("OWNER_USERNAME", "DZZD5")
ALIVE_NAME = getenv("ALIVE_NAME", "abbas")
BOT_USERNAME = getenv("BOT_USERNAME", "SDR7TBoT")
OWNER_ID = getenv("OWNER_ID", "5197215524")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "T4I4I")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DZZD5")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DZZD5")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5197215524").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
