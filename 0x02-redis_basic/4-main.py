#!/usr/bin/env python3
""" Main file """

import redis
import time
from web import get_page

# Initialize Redis
redis_store = redis.Redis()

# URL for testing
test_url = 'http://slowwly.robertomurray.co.uk'


def timed_fetch(url):
    start_time = time.time()
    content = get_page(url)
    end_time = time.time()
    duration = end_time - start_time
    return content, duration


# Fetch the page content three times to simulate different accesses
print("Fetching for the first time:")
content_first, duration_first = timed_fetch(test_url)
print(content_first[:100])  # Print the first 100 characters for brevity
print(f"Time taken: {duration_first} seconds\n")

print("Fetching for the second time (may be from cache):")
content_second, duration_second = timed_fetch(test_url)
print(content_second[:100])
print(f"Time taken: {duration_second} seconds\n")

print("Fetching for the third time (may be from cache):")
content_third, duration_third = timed_fetch(test_url)
print(content_third[:100])
print(f"Time taken: {duration_third} seconds\n")

# Retrieve count of accesses from Redis
count_key = f'count:{test_url}'
count = redis_store.get(count_key)
count = count.decode('utf-8') if count else '0'
print(f"Access count for {test_url}: {count}")

