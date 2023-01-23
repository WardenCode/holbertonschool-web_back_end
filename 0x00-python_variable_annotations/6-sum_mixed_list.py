#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and
returns their sum as a float.

You need to keep the same order to pass the checks (Union[int, float]).
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Add all elements of a list of floating or int or both

    Args:
        mxd_lst (List[Union[int, float]]): List of numbers to add

    Returns:
        float: Addition of all numbers
    """
    result: float = 0.0

    for num in mxd_lst:
        result += num

    return (result)
