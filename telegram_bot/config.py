from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    my_chat_id: str
    redis_host: str = 'localhost'
    redis_port: int = 6379


settings = Settings(_env_file='.env')
