#!/usr/bin/env python3
"""
Create a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Compute the measure of time in average of the
    coroutine wait_n

    Args:
        n (int): Call n times the function wait_random through wait_n
        max_delay (int): Set delay of each call of wait_randowm through wait_n

    Returns:
        float: Average of time of all executions
    """

    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.time() - start

    return (total_time / n)
