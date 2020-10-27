#!/usr/bin/python3
"""
    LIFOCache:
    it is a class that can
    add an item in the cache using LIFO
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
        the last element to enter is the first to leave
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if key in self.keys:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            else:
                self.keys.append(key)

            if len(self.keys) > BaseCaching.MAX_ITEMS:
                fo = self.keys.pop(len(self.keys) - 2)
                del self.cache_data[fo]
                print("DISCARD: {:s}".format(fo))

    def get(self, key):
        """
        Get an item by key
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
