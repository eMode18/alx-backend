#!/usr/bin/env python3
"""A Least Recently Used (LRU) caching module.

This module defines an `LRUCache` class that allows storing and retrieving
items from a dictionary-based cache. When the cache reaches its maximum
capacity, it removes the least recently used item (based on access order).

Attributes:
    cache_data (OrderedDict): A dictionary to store cached items with LRU
    behavior.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    def __init__(self):
        """Initializes the LRU cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache.

        Args:
            key: The identifier for the item.
            item: The value to be stored.
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(True)
            print("DISCARD:", lru_key)

    def get(self, key):
        """Retrieves an item from the cache based on its key.

        Args:
            key: The key to look up in the cache.

        Returns:
            The corresponding item if found; otherwise, None.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
