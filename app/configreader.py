from typing import Optional

from pydantic import BaseSettings, PostgresDsn, RedisDsn


class Config(BaseSettings):
    bot_token: str
    postgres_dsn: PostgresDsn
    redis_dsn: Optional[RedisDsn]
    custom_bot_api: Optional[str]
    app_host: Optional[str] = "0.0.0.0"
    app_port: Optional[int] = 9000
    webhook_domain: Optional[str]
    webhook_path: Optional[str]
    environment: Optional[str] = 'PRODUCTION'

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'


config = Config()
