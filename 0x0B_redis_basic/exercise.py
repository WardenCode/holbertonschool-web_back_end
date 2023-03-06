#!/usr/bin/env python3
"""
Definition of Cache Class
"""

from typing import Callable, Optional, Union
from uuid import uuid4

from redis import Redis


class Cache:
    """
    Cache class
    """

    def __init__(self):
        """
        Constructor of Cache class
        """
        self._redis: Redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Saves a data with a random key

        Args:
            data (Union[str, bytes, int, float]): Data
            to save on Redis

        Returns:
            str: Key of the data
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self, key: str, fn: Optional[Callable]):
        """
        Get the data saved on Redis, with a given key

        Args:
            key (str): Key of the data to be retrieved
            fn (Optional[Callable]): Callback
            function to convert the type of the data
        """
        data = self._redis.get(key)
        if (fn and data):
            return (fn(data))
        return (data)

    def get_str(self, key: str) -> Optional[str]:
        """
        Get the data saved on Redis as a string,
        with the given key

        Args:
            key (str): Key to search
            the value on Redis

        Returns:
            Optional[str]: Return the value of
            the key as a string
        """
        return (self.get(key, str))

    def get_int(self, key: str) -> Optional[int]:
        """
        Get the data saved on Redis as an int,
        with the given key

        Args:
            key (str): Key to search
            the value on Redis

        Returns:
            Optional[int]: Return the value of
            the key as a int
        """
        return (self.get(key, int))
