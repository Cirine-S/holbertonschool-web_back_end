#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union


class Cache():
    def __init__(self):
        '''store an instance of the Redis client as a private variable
        named _redis (using redis.Redis())
        and flush the instance using flushdb'''
        self._redis = redis.Redis()
        self._redis.flushdb(asynchronous=False)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' The method should generate a random key (e.g. using uuid),
        store the input data in Redis using the random key
        and return the key'''
        self.key = str(uuid.uuid4())
        self._redis.mset({self.key: data})
        return self.key
