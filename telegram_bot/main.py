import logging

from aiogram import Dispatcher, executor, types
from config import settings
from container import Container
from utils import is_token_valid_format

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)

container = Container()
container.config.set('bot_token', settings.bot_token)
dp = container.dp()


async def startup(dp: Dispatcher):
    await dp.bot.send_message(chat_id=settings.my_chat_id, text='Bot is started')
    logger.info(msg='Bot is started')
    redis_conn = await container.redis_client()
    logger.info(msg=f'Connection to redis is created: {redis_conn}')


async def shutdown(dp: Dispatcher):
    await dp.bot.send_message(chat_id=settings.my_chat_id, text='Bot is stoped')
    logger.info(msg='Bot is stoped')
    redis = await container.redis_client()
    await redis.close()


@dp.message_handler(commands=['start'])
async def accept_token(message: types.Message):
    await message.reply('Hello! Send your token pls.')


@dp.message_handler()
async def accept_token(message: types.Message):
    token = message.text
    if not is_token_valid_format(token):
        await message.reply('Invalid token format.')
        return
    chat_id = str(message.chat.id)
    sender_name: str = message.chat.first_name
    separator: str = '&'
    chat_data: str = chat_id + separator + sender_name
    redis = await container.redis_client()

    existing_value = await redis.get(token)

    if existing_value:
        if existing_value == chat_data:
            await message.reply('Token already exists.')
        else:
            await redis.set(token, chat_data)
            await message.reply('Token updated.')
    else:
        await redis.set(token, chat_data)
        await message.reply('Token accepted.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup, on_shutdown=shutdown)
