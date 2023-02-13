import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("5872722892"))
MONGO_URL = getenv("OWNER_ID", "MONGO_URL", "mongodb+srv://prova:1234@cluster0.aliaw19.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6096557808:AAGBOvloV7YoVUKitoE8J2pmx1f3lpcL6wI")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "Sono vivo")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAHIuPa76aWDUj2Ger1GhHwsSBJdNBq5Z0dkEjAC-A-WpncZgLeGOa-sXoSvOtHmRTanypDJk81rXq8_xWwPF-Me7qvhZ5mJpZCh6cMvbpOwqAPpzJmVtae6Onlpzao-wjz52wHnoY1ojdzmatdVtBrRanNEeiS46mgU9UW8tN2nRpFwdYxqtv-otjTtG74sC_D9J1UTVNIzMaezoXe4c1LMZKxVGAMHqn9E4GErj-WKCTEwA5wigSWE0GFeNer-mTivZq-IyAAdqJOWJSBJJgsd4Fro36ibuPJmAqRc0KMrDvfMvBIB1WPddMQ0ZD-gPdT7QdYn4kt-A82qHxtejcwwAAAAFeCqPMAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
