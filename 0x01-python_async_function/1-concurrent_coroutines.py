#!/usr/bin/env python3
"""
Import wait_random from the previous python file
and write an async routine called wait_n:

    async def wait_n(n: int, max_delay: int) -> list[float]

spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Calls n times the function wait_random

    Args:
        n (int): Quantity of times to call wait_random
        max_delay (int): Max delay to the calls to wait_random

    Returns:
        list[float]: List of delays on each call to wait_random function
    """

    result: list[float] = [await wait_random(max_delay) for _ in range(n)]

    return (sorted(result))
