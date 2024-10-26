import motor.motor_asyncio
from decouple import config

client = motor.motor_asyncio.AsyncIOMotorClient(config("MONGODB_URL"))
db = client.get_database(config("MONGO_DB_NAME"))

def get_db():
    return db