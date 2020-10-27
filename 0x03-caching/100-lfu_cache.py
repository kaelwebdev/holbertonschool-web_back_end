#!/usr/bin/python3
"""
    MRUCache
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    manage the cache
    """

    def __init__(self):
        """
        auto call function
        """
        super().__init__()
        self.keys = []
        self.freq = {}

    def put(self, key, item):
        """
        add an item in the cache using Least-frequently used
        """
        if key is not None and item is not None:
            if len(self.keys) >= BaseCaching.MAX_ITEMS and\
                 key not in self.keys:
                lfu = self.keys.pop(self.keys.index(self.find_lessFreq()))
                del self.freq[lfu]
                del self.cache_data[lfu]
                print("DISCARD: {:s}".format(lfu))

            self.cache_data[key] = item

            if key in self.keys:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.freq[key] += 1
            else:
                self.keys.append(key)
                self.freq[key] = 0

    def get(self, key):
        """
        Get an item by key using LFU
        """
        if not key or key not in self.cache_data:
            return None
        self.keys.append(self.keys.pop(self.keys.index(key)))
        self.freq[key] += 1
        return self.cache_data[key]

    def find_lessFreq(self):
        """
        Return key with the least frequency used
        """
        f = min(self.freq.values())
        lfu = [key for key in self.freq if self.freq[key] == f]

        for key in self.keys:
            if key in lfu:
                return key
