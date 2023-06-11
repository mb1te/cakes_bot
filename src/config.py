from pydantic import BaseSettings
from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler

from src.users import UserID


class Settings(BaseSettings):
    VK_API_TOKEN: str
    VK_GROUP_ID: str
    ORDERS_MAINTAINER: int = UserID.JULIA_NOVIKOVA.value

    class Config:
        env_file = ".env"


settings: Settings = Settings()
api = API(token=settings.VK_API_TOKEN)
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()
