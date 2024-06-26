#!/usr/bin/env python3
"""A basic caching module.

This module defines a `BasicCache` class that allows storing and retrieving
items from a dictionary-based cache.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """Adds an item to the cache.

        Args:
            key: The identifier for the item.
            item: The value to be stored.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache based on its key.

        Args:
            key: The key to look up in the cache.

        Returns:
            The corresponding item if found; otherwise, None.
        """
        return self.cache_data.get(key, None)
