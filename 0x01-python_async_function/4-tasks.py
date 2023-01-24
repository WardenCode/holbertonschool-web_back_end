#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.

The code is nearly identical to wait_n except task_wait_random is being called.
"""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Calls n times the function task_wait_random

    Args:
        n (int): Quantity of times to call task_wait_random
        max_delay (int): Max delay to the calls to task_wait_random

    Returns:
        list[float]: List of delays on each call to task_wait_random function
    """

    result: list[float] = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)]
    )

    return (sorted(result))
