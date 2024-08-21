from typing import Any

import motor.motor_asyncio as async_motor

from config.setting import settings


class MongoClient:
    client: async_motor.AsyncIOMotorClient | Any = None

    def connect(self):
        if settings.MONGO_USER.strip():
            mongo_uri = f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/"
        else:
            mongo_uri = f"mongodb://{settings.MONGO_HOST}:{settings.MONGO_PORT}/"
        self.client = async_motor.AsyncIOMotorClient(
            mongo_uri, serverSelectionTimeoutMS=10000, minPoolSize=10, maxPoolSize=50
        )[settings.MONGO_DATABASE]

    def disconnect(self):
        if self.client is not None:
            pass

    def get_client(self):
        if self.client is None:
            self.connect()
        return self.client


client = MongoClient()
