#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""

from functools import wraps
from typing import Callable, Optional

from redis import Redis
from requests import get

db: Redis = Redis()


def count_times_requested_url(func: Callable) -> Callable:
    """
    Count the times that an url was requested,
    and save on cache the HTML Content

    Args:
        func (Callable): Function to be decorated

    Returns:
        Callable: Wrapper
    """

    @wraps(func)
    def wrapper(url: str) -> str:
        """
        Logic of the decorator

        Args:
            url (str): URL to the page

        Returns:
            str: HTML content of the page
        """
        cached_url: str = "saved:{}".format(url)
        cached_reponse: Optional[bytes] = db.get(cached_url)

        if cached_reponse:
            return cached_reponse.decode("utf-8")

        url_counter_key: str = "count:{}".format(url)
        response = func(url)

        db.incr(url_counter_key)
        db.set(cached_url, response)
        db.expire(cached_url, 10)
        return response

    return wrapper


@count_times_requested_url
def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a particular UR.

    Args:
        url (str): URL to get the page

    Returns:
        str: HTML content of the URL
    """
    return get(url).text


if __name__ == '__main__':
    url = "https://www.google.com"

    # get_page("https://redis.io/commands/")
    get_page(url)
