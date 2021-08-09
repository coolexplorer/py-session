from aioredis import Redis, from_url

from config import config

configuration = config.Settings()

async def init_redis() -> Redis:
    redis = await from_url(
        url=configuration.redis_url,
        password=configuration.redis_password,
        encoding="utf-8",
        db=configuration.redis_db,
        decode_responses=True,
    )

    return redis

