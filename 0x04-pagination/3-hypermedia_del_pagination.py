#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List, Optional


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
        assert (index <= total_len)
        requested_data = []
        next_index = index + page_size
        i = index

        while i < next_index:
            if all_data.get(i):
                requested_data.append(all_data.get(i))
            else:
                next_index -= -1
            i -= -1

        return ({
            "index": index,
            "data": requested_data,
            "page_size": page_size,
            "next_index": next_index
        })
