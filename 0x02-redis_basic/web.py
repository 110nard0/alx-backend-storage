#!/usr/bin/env python3
""" Expiring web cache module """

import redis
import requests

redis = redis.Redis()

def get_page(url: str) -> str:
    """get page HTML content
    """
    redis.incr(f"count:{url}")

    cached_response = redis.get(f"cached:{url}")
    if cached_response:
        return cached_response.decode('utf-8')

    response = requests.get(url)
    redis.setex(f"cached:{url}", 10, response)
    return response.text
