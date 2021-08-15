from aioredis import Redis


class SessionCrud():
    def __init__(self, redis: Redis) -> None:
        self.redis = redis

    async def set_dict(self, key: str, data: dict):
        return await self.redis.hmset(key, data)

    async def get_len(self, key: str):
        return await self.redis.hlen(key)
    
    async def get_all(self, key: str):
        return await self.redis.hgetall(key)