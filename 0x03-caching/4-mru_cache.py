#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from
BaseCaching and is a caching system
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Caching system with limit of 4 elements and
    using the Cache replacement policies - MRU
    """

    def __init__(self):
        """
        Construsctor of MRUCache Class
        and call to init function of
        BaseCaching Class
        """
        self.recently_used = []
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key 'key'.

        Taking in acount the limitations of the cache, and
        the cache replacement Policy of MRU.

        When an item is deleted, print a message

        Args:
            key (str): Key to put inside cache_data
            item (Any): Value to put inside cache_data
        """
        if (not key or not item):
            return

        if (self.cache_data.get(key)):
            position = self.recently_used.index(key)
            moved_value = self.recently_used.pop(position)
            self.recently_used.append(moved_value)
        else:
            self.recently_used.append(key)

        self.cache_data[key] = item
        len_cache_data = len(self.cache_data)

        if (len_cache_data > self.MAX_ITEMS):
            eliminated = self.recently_used.pop(-2)
            del self.cache_data[eliminated]
            print("DISCARD: {}".format(eliminated))

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

        value = self.cache_data.get(key)

        if (value):
            position = self.recently_used.index(key)
            moved_value = self.recently_used.pop(position)
            self.recently_used.append(moved_value)

        return (value)
