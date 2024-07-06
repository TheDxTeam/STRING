from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID" , 25511402))
API_HASH = getenv("API_HASH","73cd4400a9f1215c598e4a8549b39c87")

BOT_TOKEN = getenv("BOT_TOKEN","6931836501:AAFIajWfNVoDl0m7lLSupp5KFZS4c8M1V90")
OWNER_ID = int(getenv("OWNER_ID",6535576719))

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Cuteboy:Cuteboy@cuteboy0.dmuoa90.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "THE_CUTE_BOY_OP")
