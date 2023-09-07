import asyncio

from aiogram import Bot
from redis import Redis

from api.exceptions import UserEmptyTokenException, ChatIdNodFoundException


class MessageSenderService:
    def __init__(self, redis_conn: Redis, bot_token: str):
        self.redis = redis_conn
        self.bot_token = bot_token
        self.chat_id: str | None = None
        self.chat_name: str | None = None

    def get_user_chat_id(self, user_token: str | None) -> None:
        if not user_token:
            raise UserEmptyTokenException('User does not have a token.')
        chat_data: str = self.redis.get(user_token)
        if chat_data is None:
            raise ChatIdNodFoundException('Send token to bot.')
        chat_data_list = chat_data.split(sep='&', maxsplit=1)
        self.chat_id = chat_data_list[0]
        self.chat_name = chat_data_list[1]

    async def _send_message(self, user_message: str):
        bot = Bot(token=self.bot_token)
        message_template = '{user_name}, я получил от тебя сообщение:\n{message}'
        message = message_template.format(user_name=self.chat_name, message=user_message)
        try:
            await bot.send_message(self.chat_id, message)
        finally:
            await bot.close()

    def send_message(self, message: str):
        asyncio.run(self._send_message(message))
