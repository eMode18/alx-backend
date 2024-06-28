#!/usr/bin/env python3
"""Least Frequently Used caching module.

This module defines an `LFUCache` class that allows storing and retrieving
items from a dictionary-based cache. When the cache reaches its maximum
capacity, it removes the least frequently used item
(based on access frequency).

Attributes:
    cache_data (OrderedDict): A dictionary to store cached items with LFU
    behavior.
    keys_freq (list): A list to track the frequency of each cache key.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching and uses LFU algorithm.
    """

    def __init__(self):
        """
        Initialize the LFU cache.
        """
        super().__init__()
        self.usage_count = {}

    def put(self, key, item):
        """
        Add an item to the cache using LFU algorithm.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
            If the cache size exceeds BaseCaching.MAX_ITEMS, discard the least
            frequently used item.
            If multiple items have the same least frequency, use LRU algorithm
            to break ties.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_usage = min(self.usage_count.values())
                least_frequent_keys = [k for k, v in self.usage_count.items()
                                       if v == min_usage]

                lru_key = self.usage_order.pop(0)
                while lru_key not in least_frequent_keys:
                    lru_key = self.usage_order.pop(0)

                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
                del self.usage_count[lru_key]

            self.cache_data[key] = item
            self.usage_order.append(key)
            self.usage_count[key] = self.usage_count.get(key, 0) + 1

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value associated with the key, or None if not found.
        """
        if key in self.cache_data:
            self.usage_count[key] += 1
            return self.cache_data[key]
        return None
