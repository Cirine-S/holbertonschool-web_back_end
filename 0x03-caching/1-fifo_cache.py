#!/usr/bin/python3
'''BasicCache module'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''''BasicCache class'''''

    def put(self, key, item):
        '''Add an item in the cache'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            ItemToDiscard = sorted(self.cache_data)[0]
            print('DISCARD: {}'.format(ItemToDiscard))
            self.cache_data.pop(ItemToDiscard)
        self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key'''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
