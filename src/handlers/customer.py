from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler

from src.rules import CustomerMessageRule
from src.utils import send_message_to_maintainer

customer_labeler = BotLabeler()


@customer_labeler.private_message(CustomerMessageRule())
async def process_customer_message(message: Message):
    print("customer: ", message)
    await send_message_to_maintainer(message.id)
