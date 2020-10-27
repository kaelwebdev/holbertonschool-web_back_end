#!/usr/bin/python3
"""
    FIFOCache:
    it is a class that can
    add an item in the cache using FIFO
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
        the first element to enter is the first to leave
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                fo = self.keys.pop(0)
                del self.cache_data[fo]
                print("DISCARD: {:s}".format(fo))

    def get(self, key):
        """
        Get an item by key
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
