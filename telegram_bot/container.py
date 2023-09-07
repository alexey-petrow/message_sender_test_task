from dependency_injector import containers, providers
from redis.asyncio.client import Redis
from aiogram import Bot, Dispatcher

from config import settings


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    redis_client = providers.Singleton(
        Redis,
        host=settings.redis_host,
        port=settings.redis_port,
        decode_responses=True,
    )
    bot_client = providers.Singleton(Bot, token=config.bot_token)
    dp = providers.Singleton(Dispatcher, bot=bot_client)
