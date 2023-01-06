import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "22165592")) #optional
API_HASH = getenv("API_HASH", "aa2886eda514d8beaa98695cfe3060ff") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5945209516").split()))
OWNER_ID = int(getenv("OWNER_ID","5945209516"))
MONGO_URL = getenv("MONGO_URL","mongodb://aryauserbot:aryauserbot@cluster0-shard-00-00.w6kd5.mongodb.net:27017,cluster0-shard-00-01.w6kd5.mongodb.net:27017,cluster0-shard-00-02.w6kd5.mongodb.net:27017/?ssl=true&replicaSet=atlas-rjm594-shard-0&authSource=admin&retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5818606596:AAHwH17M5L3SSX_XxSAZ2OXxxrPk2M3gjvg")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER","687154450")
LOG_GROUP = getenv("LOG_GROUP","687154450")
GIT_TOKEN = getenv("GIT_TOKEN","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") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBqdJFhzx3RvtPbTm97rFeP_tgBD1OwcNzHvqAKK35NIrusT2ehhhh1g2GbeEfMJGvu1QDUM1IjKQZclsYhj-DmUs3WK58YCUUfT7ZvAZuqO_8jrKAEA5bAoy44YIymkMGQPrfNqYW6bWelpHVbGs0vtvVNez2Uzzu3I-OSamdj1FXHblnMFXOBaF-Em4ch5qMFyOMeDyUS_0RXmmqIzfnuGalzm4j6sWXMP0EzOXjzvqnJ_Wyx7QZ7Wo-YzlSHNu3_amaMXAKmPw2Syi1PWvg7edRJUYNzNIs0vbJ5x9GUQ-XzQBD0yDcTwi9JkmbPGYWHHpGyPwJJ5bWrdnZBhFh8AAAAAWJcsqwA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
