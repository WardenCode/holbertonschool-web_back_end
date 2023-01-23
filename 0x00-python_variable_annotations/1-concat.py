#!/usr/bin/env python3
"""
Type-annotated function concat that
takes a string str1 and a string str2 as arguments and
returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings

    Args:
        str1 (str): First string to be concatenated
        str2 (str): Second strign to be concatenated

    Returns:
        str: str1 and str2 concatenated
    """
    return (str1 + str2)
