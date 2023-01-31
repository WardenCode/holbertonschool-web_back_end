#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Tuple, Union


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

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Get page size elements from index, regardless if any were deleted

        Args:
            index (int, optional): Index to get. Defaults to None.
            page_size (int, optional): Size of Page. Defaults to 10.

        Returns:
            Dict: Data from index to index + page_size
        """
        # all_data = self.indexed_dataset()
        # total_len = len(all_data)
        # assert (index <= total_len)
        # next_index = index + page_size
        # requested_data = []
        # i = index

        # while i < next_index:
        #     if all_data.get(i):
        #         requested_data.append(all_data.get(i))
        #     else:
        #         next_index += 1
        #     i += 1

        # return ({
        #     "index": index,
        #     "data": requested_data,
        #     "page_size": page_size,
        #     "next_index": next_index
        # })
        dataset = self.indexed_dataset()
        assert (index <= len(dataset))
        next_index = index + page_size
        returned_data = []
        current_idx = index

        while current_idx < next_index:
            if dataset.get(current_idx):
                returned_data.append(dataset.get(current_idx))
            else:
                next_index -= -1
            current_idx -= -1

        data = {
            'index': index,
            'data': returned_data,
            'page_size': page_size,
            'next_index': next_index,
        }

        return data
