#!/usr/bin/env python3
"""Module exercise"""

import redis
from typing import Union
from uuid import uuid4


class Cache:
    """Cache class for storing user data"""
    def __init__(self):
        """Initializes a Cache class instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, float, int, str]) -> str:
        """Generates a random key and stores input in Redis cache

        Argument:
            data (any): user input

        Returns:
            key (str): key hash mapped to stored Redis value
        """
        rand_key = str(uuid4())
        self._redis.set(rand_key, data)
        return rand_key
