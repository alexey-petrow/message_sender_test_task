from dependency_injector import containers, providers
from redis import Redis

from api.services import MessageSenderService


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    redis_client = providers.Singleton(
        Redis,
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        decode_responses=True,
    )

    message_sender_service = providers.Factory(
        MessageSenderService,
        redis_conn=redis_client,
        bot_token=config.TELEGRAM_BOT_TOKEN,
    )
