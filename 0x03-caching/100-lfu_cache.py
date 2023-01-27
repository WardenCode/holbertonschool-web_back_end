#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from
BaseCaching and is a caching system
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Caching system with limit of 4 elements and
    using the Cache replacement policies - LFU
    """

    def __init__(self):
        """
        Construsctor of LFUCache Class
        and call to init function of
        BaseCaching Class
        """
        self.element_frequency = {}
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key 'key'.

        Taking in acount the limitations of the cache, and
        the cache replacement Policy of LFU.

        When an item is deleted, print a message

        Args:
            key (str): Key to put inside cache_data
            item (Any): Value to put inside cache_data
        """
        if (not key or not item):
            return

        copy_before_new_element = dict.copy(self.element_frequency)

        self.element_frequency[key] = (
            self.element_frequency.get(key) or 0) + 1

        self.cache_data[key] = item
        len_cache_data = len(self.cache_data)

        if (len_cache_data > self.MAX_ITEMS):
            min_item_key = min(
                copy_before_new_element.items(), key=lambda x: x[1])[0]
            del self.element_frequency[min_item_key]
            del self.cache_data[min_item_key]
            print("DISCARD: {}".format(min_item_key))

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
            self.element_frequency[key] += 1

        return (value)
