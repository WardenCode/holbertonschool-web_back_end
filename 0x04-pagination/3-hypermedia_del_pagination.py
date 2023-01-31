#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Any, Dict, List, Optional


def rounded_binary_search(numbers: List[int], search: int) -> int:
    """
    Search a number on array, if doesn't exist,
    return the closest one

    Args:
        numbers (List[int]): List of ordered numbers
        search (int): Number to search

    Returns:
        int: Index where is the number
    """
    high: int = len(numbers) - 1
    low: int = 0
    idx: int = 0

    while (numbers[idx] != search):
        idx = int((high - low) / 2) + low

        if (numbers[idx] == search):
            return (idx)

        if (low == high):
            break

        if (numbers[idx] < search):
            low = idx + 1
        else:
            high = idx - 1

    return (idx + 1)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """
        Get page size elements from index, regardless if any were deleted

        Args:
            index (int, optional): Index to get. Defaults to None.
            page_size (int, optional): Size of Page. Defaults to 10.

        Returns:
            Dict: Data from index to index + page_size
        """
        all_data = self.indexed_dataset()
        total_len = len(all_data)
        assert isinstance(index, int) and 0 <= index <= total_len
        ids = list(all_data.keys())
        requested_data = []
        last_idx = 0

        closest_idx = rounded_binary_search(ids, index)

        for i in range(closest_idx, closest_idx + page_size):
            if (i > total_len):
                break
            requested_data.append(all_data[ids[i]])
            last_idx = ids[i]

        return ({
            "index": index,
            "data": requested_data,
            "page_size": len(requested_data),
            "next_index": last_idx + 1 if last_idx + 1 < total_len else None
        })
