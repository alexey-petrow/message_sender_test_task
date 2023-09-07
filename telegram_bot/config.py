from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    bot_token: str = Field(alias='TELEGRAM_BOT_TOKEN')
    my_chat_id: str
    redis_host: str = 'localhost'
    redis_port: int = 6379

    model_config = ConfigDict(extra='allow')


settings = Settings(_env_file='.env')
