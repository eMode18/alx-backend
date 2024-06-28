#!/usr/bin/env python3
"""A Most Recently Used (MRU) caching module.

This module defines an `MRUCache` class that allows storing and retrieving
items from a dictionary-based cache. When the cache reaches its maximum
capacity, it removes the most recently used item (based on access order).

Attributes:
    cache_data (OrderedDict): A dictionary to store cached items with MRU
    behavior.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching and uses MRU algorithm.
    """

    def __init__(self):
        """
        Initialize the MRU cache.
        """
        super().__init__()  # Call the parent class constructor
        self.usage_order = []  # Maintain order of keys based on usage

    def put(self, key, item):
        """
        Add an item to the cache using MRU algorithm.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
            If the cache size exceeds BaseCaching.MAX_ITEMS, discard
            the most recently used item.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item
                mru_key = self.usage_order.pop()
                print(f"DISCARD: {mru_key}")
                del self.cache_data[mru_key]
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value associated with the key, or None if not found.
        """
        if key in self.cache_data:
            # Update usage order (move key to the end)
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
