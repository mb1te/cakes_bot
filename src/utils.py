import json

from vkbottle import API

from config import settings

api = API(token=settings.VK_API_TOKEN)


async def send_message_to_maintainer(msg_id: int):
    await api.messages.send(
        peer_id=settings.ORDERS_MAINTAINER, forward_messages=[msg_id], random_id=0
    )


async def send_message_to_customer(response: str, msg_id: int, peer_id: int):
    await api.messages.send(
        peer_id=peer_id,
        message=response,
        forward=json.dumps(
            {
                "message_ids": [msg_id],
                "peer_id": peer_id,
                "is_reply": True,
            }
        ),
        random_id=0,
    )
