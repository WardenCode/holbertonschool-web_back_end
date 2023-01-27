#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Caching system with limit of 4 elements and
    using the Cache replacement policies - FIFO
    """

    def __init__(self):
        """
        Construsctor of FIFOCache Class
        and call to init function of
        BaseCaching Class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key 'key'.

        Taking in acount the limitations of the cache, and
        the cache replacement Policiy of FIFO.

        When an item is deleted, print a message

        Args:
            key (str): Key to put inside cache_data
            item (Any): Value to put inside cache_data
        """
        if (not key or not item):
            return

        self.cache_data[key] = item
        len_cache_data = len(self.cache_data)

        if (len_cache_data > self.MAX_ITEMS):
            to_delete = next(iter(self.cache_data))
            del self.cache_data[to_delete]
            print("DISCARD: {}".format(to_delete))

    def get(self, key):
        """
        Gets the value in self.cache_data linked to key.

        Args:
            key (str): Key to search inside cache_data

        Returns:
            value: If value is founded is returned,
            None otherwise.
        """
        if (key is None):
            return (None)

        return (self.cache_data.get(key))
