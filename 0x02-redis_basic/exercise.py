#!/usr/bin/env python3
"""
0. Writing strings to Redis
1. Reading from Redis and recovering original type
2. Incrementing values
3. Storing lists
4. Retrieving lists
"""
import redis
import uuid


class Cache:
    """
    Cache class
    """

    def __init__(self):
        """
        In the __init__ method, store an instance of the Redis client
        as a private variable named _redis (using redis.Redis()) and
        flush the instance using flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
         """
         Store data in the cache.
         """
         return self._redis.set(str(uuid.uuid4()), data)