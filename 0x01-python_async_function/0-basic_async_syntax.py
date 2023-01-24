#!/usr/bin/env python3
"""
Asynchronous coroutine:
    async def wait_random(max_delay: int) -> float:
waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually
returns it.

Use the random module.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits a random amout of time
    and return that time

    Args:
        max_delay (int, optional): Max delay for wait. Defaults to 10.

    Returns:
        float: Amout of time waited
    """

    value: float = random.uniform(0, max_delay)

    await asyncio.sleep(0.0, value)

    return (value)
