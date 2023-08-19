#!/usr/bin/env python3
"""Module exercise contains a Redis cache class and [decorator] functions"""

import redis
from functools import wraps
from typing import Callable, Optional, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """Decorator function

    Argument:
        method (Callable): Cache class instance method

    Returns:
        increment_func (Callable): wrapper function
    """
    key = method.__qualname__

    @wraps(method)
    def increment_func(self, *args, **kwargs):
        """Increments the count for method key on every method call

        Return: value returned by original method
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return increment_func


def call_history(method: Callable) -> Callable:
    """Decorator function

    Argument:
        method (Callable): Cache class instance method

    Returns:
        wrapper_func (Callable): wrapper function
    """
    inkey = f"{method.__qualname__}:inputs"
    outkey = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper_func(self, *args, **kwargs):
        """Stores the history of inputs and outputs for a particular method

        Return: value returned by original method
        """
        self._redis.rpush(inkey, str(args))
        value = method(self, *args, **kwargs)
        self._redis.rpush(outkey, value)

        return value

    return wrapper_func


def replay(store: Callable):
    """
    """
    cache = store.__self__
    name = store.__qualname__

    input_key = f"{name}:inputs"
    output_key = f"{name}:outputs"

    inputs = cache._redis.lrange(f"{input_key}", 0, -1)
    outputs = cache._redis.lrange(f"{output_key}", 0, -1)

    print(f"{name} was called {len(inputs)} times:")

    for input, output in zip(inputs, outputs):
        input_str = input.decode("utf-8")
        output_str = output.decode("utf-8")
        print(f"{name}(*{input_str}) -> {output_str}")


class Cache:
    """Cache class for storing user data"""
    def __init__(self):
        """Initializes a Cache class instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
