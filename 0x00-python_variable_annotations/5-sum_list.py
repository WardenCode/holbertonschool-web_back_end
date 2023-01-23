#!/usr/bin/env python3
"""
Type-annotated function sum_list which
takes a list input_list of floats as argument and
returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Add all elements of a list of floating numbers

    Args:
        input_list (List[float]): List of floating numbers

    Returns:
        float: The sum of all elements on the list
    """
    result: float = 0.0

    for num in input_list:
        result += num

    return (result)
