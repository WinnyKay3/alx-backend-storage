#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """
    A decorator to cache the output of a function
    (specifically designed for get_page).
    It uses Redis to store the cached data and the
    count of URL accesses.
    """

    @wraps(method)
    def invoker(url: str) -> str:
        """
        The wrapper function around the actual function call.
        It manages caching and counting of URL accesses.
        :param url: The URL to be fetched.
        :return: The content of the URL, either from
        the cache or fetched directly.
        """
        # Increment the access count for the given URL in Redis
        redis_store.incr(f'count:{url}')

        # Try to retrieve the cached result from Redis
        cached_result = redis_store.get(f'result:{url}')
        if cached_result:
            # If cached result exists, return it after decoding
            return cached_result.decode('utf-8')

        # If not cached, call the actual function to fetch the data
        result = method(url)
        # Store the fetched result in Redis with an expiration
        # time of 10 seconds
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """
    Fetches the content of a given URL.
    This function is wrapped by the data_cacher decorator,
    which adds caching and access counting functionality.
    :param url: The URL whose content is to be fetched.
    :return: The content of the URL as a string.
    """
    # Make an HTTP GET request to the specified URL and
    # return its text content
    return requests.get(url).text
