#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds,
explain it to yourself.
"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Compute the amout of time to exectute async_comprehension()
    four times using asyncio.gather function.

    Returns:
        float: Amout of time.
    """

    start = time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time()

    return (end - start)
