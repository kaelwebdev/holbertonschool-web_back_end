#!/usr/bin/python3
"""
    LRUCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    manage the cache
    """

    def __init__(self):
        """
        auto call function
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        discard least recently used items first
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if key in self.keys:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            else:
                self.keys.append(key)

            if len(self.keys) > BaseCaching.MAX_ITEMS:
                lru = self.keys.pop(0)
                del self.cache_data[lru]
                print("DISCARD: {:s}".format(lru))

    def get(self, key):
        """
        Get an item by key using LRU
        """
        if not key or key not in self.cache_data:
            return None
        self.keys.append(self.keys.pop(self.keys.index(key)))
        return self.cache_data[key]
