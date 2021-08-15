from aioredis import Redis, from_url

from config import config

settings = config.Settings()

async def init_redis() -> Redis:
    redis = await from_url(
        url=settings.redis_url,
        password=settings.redis_password,
        encoding="utf-8",
        db=settings.redis_db,
        decode_responses=True,
    )

    return redis

