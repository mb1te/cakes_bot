from vkbottle import ABCRule
from vkbottle.bot import Message

from config import settings


class MaintainerMessageRule(ABCRule):
    async def check(self, event: Message) -> bool:
        return event.from_id == settings.ORDERS_MAINTAINER
