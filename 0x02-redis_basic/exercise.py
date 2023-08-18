#!/usr/bin/env python3
"""Module exercise"""

import redis
import uuid


class Cache():
    """Cache class for storing user variables"""
    def __init__(self):
        """Initializes a Cache class instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        """Generates a random key and stores input in Redis cache

        Argument:
            data (any): user input

        Returns:
            key (str): key hash mapped to stored Redis value
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
