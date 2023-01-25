#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously
wait 1 second,then yield a random number between 0 and 10.

Use the random module.
"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generator of random float numbers

    Returns:
        Generator[float, None, None]: Random float numbers
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield (uniform(0, 10))
