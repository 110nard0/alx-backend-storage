#!/usr/bin/env python3
"""Module exercise"""

import redis
from typing import Callable, Optional, Union
from uuid import uuid4


class Cache:
    """Cache class for storing user data"""
    def __init__(self):
        """Initializes a Cache class instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores input in Redis cache

        Argument:
            data (any): user input

        Returns:
            key (str): key hash mapped to stored Redis value
        """
        rand_key = str(uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        """Returns value associated with Redis key or None if nil

        Args:
            key (str): key to stored value in Redis cache
            fn (Callable): Optional function to convert data to desired format

        Returns:
            value (any): value stored in Redis cache of default str type
        """
        value = self._redis.get(key)
        if value and fn is not None:
            value = fn(value)
        return value

    def get_int(self, key: str) -> int:
        """Automatically parametrizes Cache.get method with the
        appropriate conversion function

        Argument:
            key (str): key to stored value in Redis cache

        Returns:
            (int): integer value
        """
        return self.get(key, int)

    def get_str(self, key: str) -> str:
        """Automatically parametrizes Cache.get method with the
        appropriate conversion function

        Argument:
            key (str): key to stored value in Redis cache

        Returns:
            (str): string value
        """
        return self.get(key, lambda d: d.decode('utf-8'))
