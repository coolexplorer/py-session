import logging
import os
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    redis_url: AnyUrl = os.getenv('REDIS_URL', 'redis://localhost')
    redis_password: str = os.getenv('REDIS_PASSWORD', 'redis_password')
    redis_db: int = int(os.getenv("REDIS_DB", "0"))
    auth_address: str = os.getenv('AUTH_ADDRESS', 'localhost:8080')
    auth_api_version: int = int(os.getenv('AUTH_API_VERSION', '1'))

@lru_cache
def get_setting() -> BaseSettings:
    logger.info('Loading configurations from environment')
    return Settings()