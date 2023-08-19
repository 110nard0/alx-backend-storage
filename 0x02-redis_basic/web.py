#!/usr/bin/env python3
"""Module web"""

import redis
import requests
from datetime import timedelta
from functools import wraps

r = redis.Redis()


def count_url(method):
    """Decorator function that tracks the frequency with which
        a particular URL is accessed
    """
    @wraps(method)
    def wrapper(url):
        """wrapper function"""
        r.incr(method.__qualname__)
        r.incr(f"count:{url}")
        return method(url)
    return wrapper


def cache_page(method):
    """Decorator function that stores a web page in a Redis cache with
        a 10 seconds expiration or returns a cached version if present
    """
    @wraps(method)
    def wrapper(url):
        """wrapper function"""
        cached_page = r.get(url)
        if cached_page:
            return cached_page.decode('utf-8')
        else:
            page = method(url)
            r.setex(url, timedelta(seconds=10), value=page)
            return page
    return wrapper


@count_url
@cache_page
def get_page(url: str) -> str:
    """Gets the HTML content of a particular URL using requests module
    """
    page = requests.get(url).text
    return page
