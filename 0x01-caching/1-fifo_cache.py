#!/usr/bin/env python3
"""A First-In First-Out (FIFO) caching module.

This module defines an `FIFOCache` class that allows storing and retrieving
items from a dictionary-based cache. When the cache reaches its maximum
capacity, it removes the oldest item (based on insertion order).

Attributes:
    cache_data (OrderedDict): A dictionary to store cached items with
    FIFO behavior.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    def __init__(self):
        """Initializes the FIFO cache."""
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
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item from the cache based on its key.

        Args:
            key: The key to look up in the cache.

        Returns:
            The corresponding item if found; otherwise, None.
        """
        return self.cache_data.get(key, None)
