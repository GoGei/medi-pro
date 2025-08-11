import json
from django_redis import get_redis_connection


class BaseRedis:
    KEY: str = ''
    TTL: int | None = None

    def __init__(self, *args, **kwargs):
        self.redis = get_redis_connection("default")
        self.key = self.KEY.format(*args, **kwargs)

    def set(self, value):
        self.redis.set(self.key, json.dumps(value), ex=self.TTL)

    def get(self) -> dict | None:
        data = self.redis.get(self.key)
        return None if data is None else json.loads(data)


class TestRedis(BaseRedis):
    KEY = 'test:{key}'
    TTL = 60
