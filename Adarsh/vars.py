# (c) ANURAG-MAHESWARI
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '15939361'))
    API_HASH = str(getenv('API_HASH', 'f8beb0bd0054a717d84fbe9be12a23ea'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5735446073:AAFlSXk_I8B-YEQMH6vStsjeyvxbg6SyBw0'))
    name = str(getenv('SESSION_NAME', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '1'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001527701055'))
    PORT = int(getenv('PORT', '8989'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '3.110.81.27'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5543917190").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'am_robots'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '3.110.81.27:8989')) if not ON_HEROKU or getenv('FQDN', '3.110.81.27:8989') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://rename:rename@cluster0.f0vmafy.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', '-1001744824600'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001527701055")).split())) 
