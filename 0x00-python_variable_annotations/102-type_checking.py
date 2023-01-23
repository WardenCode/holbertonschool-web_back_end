#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code
and apply any necessary changes.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Take a tuple and repeat each element by factor creating a list

    Args:
        lst (Tuple): Tuple with elements to repeat
        factor (int, optional): Number of times to repeat
        each element of the tuple. Defaults to 2.

    Returns:
        List: Return a zoomed list (duplicate each element)
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return (zoomed_in)
