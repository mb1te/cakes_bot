from vkbottle import Bot

from config import api, labeler, state_dispenser
from handlers import customer_labeler, maintainer_labeler

labeler.load(customer_labeler)
labeler.load(maintainer_labeler)

bot = Bot(
    api=api,
    labeler=labeler,
    state_dispenser=state_dispenser,
)
bot.run_forever()
