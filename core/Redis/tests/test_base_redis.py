from django.test import TestCase
from ..base import TestRedis


class TestRedisTestCase(TestCase):
    def test_redis(self):
        cls = TestRedis(key='test')
        self.assertFalse(cls.get())
        self.assertFalse(cls.exists())
        cls.set(1)
        self.assertTrue(cls.get())
        self.assertTrue(cls.exists())
        cls.delete()
        self.assertFalse(cls.get())
        self.assertFalse(cls.exists())
