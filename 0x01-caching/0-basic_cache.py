#!/usr/bin/env python3
"""A basic caching module.

This module defines a `BasicCache` class that allows storing and retrieving
items from a dictionary-based cache.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching system that inherits from BaseCaching.
    This cache has no size limit.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
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
