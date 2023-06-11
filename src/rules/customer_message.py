from vkbottle import ABCRule
from vkbottle.bot import Message

from src.config import settings


class CustomerMessageRule(ABCRule[Message]):
    async def check(self, event: Message) -> bool:
        return event.from_id != settings.ORDERS_MAINTAINER
