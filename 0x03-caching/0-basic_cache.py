#!/usr/bin/env python3
"""
Create a class BasicCache that inherits
from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This caching system doesn't have limit
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the
        item value for the key 'key'.

        Args:
            key (str): Key to put inside cache_data
            item (Any): Value to put inside cache_data
        """

        if (key and item):
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets the value in self.cache_data linked to key.

        Args:
            key (str): Key to search inside cache_data

        Returns:
            value: If value is founded is returned, None otherwise.
        """
        if (key is None):
            return (None)

        return (self.cache_data.get(key))
