from redis import Redis
from django.conf import settings


class BaseRedis(object):
    KEY = 'key'
    TTL = 60

    def __init__(self, **kwargs):
        self.key = self.KEY.format(**kwargs)

    @classmethod
    def get_default_redis_conn(cls, **kwargs) -> Redis:
        if settings.REDIS_HOST:
            kwargs['host'] = settings.REDIS_HOST
        if settings.REDIS_PORT:
            kwargs['port'] = settings.REDIS_PORT
        if settings.REDIS_PASS:
            kwargs['password'] = settings.REDIS_PASS
        return Redis(**kwargs)

    def set(self, value):
        with self.get_default_redis_conn() as r:
            return r.set(name=self.key, value=value, ex=self.TTL)

    def get(self) -> bytes:
        with self.get_default_redis_conn() as r:
            return r.get(self.key)

    def delete(self):
        with self.get_default_redis_conn() as r:
            return r.delete(self.key)

    def exists(self):
        with self.get_default_redis_conn() as r:
            return r.exists(self.key)
