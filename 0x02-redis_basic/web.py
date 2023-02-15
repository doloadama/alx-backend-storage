#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import requests
import redis
import time
from functools import wraps


# create Redis client
redis_client = redis.Redis(host='localhost', port=6379)

def get_page(url: str) -> str:
    # check if the page is already cached
    cached_page = redis_client.get(url)
    if cached_page is not None:
        return cached_page.decode('utf-8')
    
    # page not cached, fetch from web and cache it
    response = requests.get(url)
    page = response.text
    
    # track the number of times the page is accessed
    count_key = f"count:{url}"
    redis_client.incr(count_key)

    # cache the page with expiration time of 10 seconds
    redis_client.setex(url, 10, page)
    
    return page

def cache_with_expiration_time(expiration_time):
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            cached_page = redis_client.get(url)
            if cached_page is not None:
                return cached_page.decode('utf-8')

            response = func(url)
            redis_client.setex(url, expiration_time, response)
            return response
        return wrapper
    return decorator

@cache_with_expiration_time(10)
def get_page_with_cache(url: str) -> str:
    response = requests.get(url)
    page = response.text
    return page
