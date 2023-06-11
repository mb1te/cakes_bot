from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler

from rules import MaintainerMessageRule
from utils import send_message_to_customer

maintainer_labeler = BotLabeler()


@maintainer_labeler.private_message(MaintainerMessageRule())
async def process_customer_message(message: Message):
    if not message.reply_message or not message.reply_message.fwd_messages:
        await message.reply(
            "Я умею только пересылать ответ пользователю, используйте кнопку"
            "<<Ответить>> на пересланное сообщение от имени группы"
        )
        return

    reply_message = message.reply_message.fwd_messages[0]
    await send_message_to_customer(
        response=message.text, msg_id=reply_message.id, peer_id=reply_message.peer_id
    )
    await message.reply("Ответ успешно отправлен")
