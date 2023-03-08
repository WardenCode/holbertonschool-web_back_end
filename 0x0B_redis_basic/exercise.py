#!/usr/bin/env python3
"""
Definition of Cache Class
"""

import uuid
from functools import wraps
from typing import Callable, List, Optional, Union

import redis


def replay(method: Callable):
    """
    Shows the times that a method was called
    as a replay

    Args:
        method (Callable): Method to be replaied
    """
    db: redis.Redis = redis.Redis()
    key: str = method.__qualname__

    input_key: str = "{}:inputs".format(key)
    output_key: str = "{}:outputs".format(key)

    inputs: List[bytes] = db.lrange(input_key, 0, -1)
    outputs: List[bytes] = db.lrange(output_key, 0, -1)

    count: str = db.get(key).decode('utf-8')

    print("{} was called {} times:".format(key, count))

    for input, output in zip(inputs, outputs):
        input = input.decode('utf-8')
        output = output.decode('utf-8')
        print("{}(*{}) -> {}".format(key, input, output))


def call_history(method: Callable) -> Callable:
    """
    Decorator that saves the call history of a given method
    saves on redis, a list of a input and output of the method

    Args:
        method (Callable): Method to be decorated

    Returns:
        Callable: Wrapped Method
    """
    key: str = method.__qualname__
    input_key: str = "{}:inputs".format(key)
    output_key: str = "{}:outputs".format(key)

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper that saves the history on redis
        inputs and outputs
        """
        self._redis.rpush(input_key, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(output_key, res)
        return res

    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the times that
    a method is called
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Logig of the decorator that counts
        the times that a method is called
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    Cache class
    """

    def __init__(self):
        """
        Constructor of Cache class
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Saves a data with a random key

        Args:
            data (Union[str, bytes, int, float]): Data
            to save on Redis

        Returns:
            str: Key of the data
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        Get the data saved on Redis, with a given key

        Args:
            key (str): Key of the data to be retrieved
            fn (Optional[Callable]): Callback
            function to convert the type of the data
        """
        data = self._redis.get(key)
        if (fn):
            return fn(data)
        return data

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
        return self.get(key, str)

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
        return self.get(key, int)
