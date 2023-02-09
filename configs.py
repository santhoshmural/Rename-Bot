# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "11319890"))
    API_HASH = os.environ.get("API_HASH", "4965e574411647c42ffbd8b46040f0a5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6056424899:AAHHVaeFgUHAn9bqIlEpGvXJIzV0hCRRu8o")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", "1365582907"))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "1365582907").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Indonesia:indonesia37@cluster0.7gxmrjn.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001532796897"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
