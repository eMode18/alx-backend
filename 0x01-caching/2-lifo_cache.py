#!/usr/bin/env python3
"""A Last-In First-Out (LIFO) caching module.

This module defines an `LIFOCache` class that allows storing and retrieving
items from a dictionary-based cache. When the cache reaches its maximum
capacity, it removes the most recently added item (based on insertion order).

Attributes:
    cache_data (OrderedDict): A dictionary to store cached items with LIFO
    behavior.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching and uses LIFO algorithm.
    """

    def __init__(self):
        """
        Initialize the LIFO cache.
        """
        super().__init__()  # Call the parent class constructor

    def put(self, key, item):
        """
        Add an item to the cache using LIFO algorithm.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
            If the cache size exceeds BaseCaching.MAX_ITEMS, discard
            the last item.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = next(reversed(self.cache_data))
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value associated with the key, or None if not found.
        """
        return self.cache_data.get(key)
