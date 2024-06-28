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


class FIFOCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching and uses FIFO algorithm.
    """

    def __init__(self):
        """
        Initialize the FIFO cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using FIFO algorithm.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
            If the cache size exceeds BaseCaching.MAX_ITEMS, discard the
            oldest item.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                print(f"DISCARD: {oldest_key}")
                del self.cache_data[oldest_key]
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
