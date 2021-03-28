#!/usr/bin/python3
'''BasicCache module'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''''BasicCache class'''''
    LAST_IN = ''

    def put(self, key, item):
        '''Add an item in the cache'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                print('DISCARD: {}'.format(self.__class__.LAST_IN))
                self.cache_data.pop(self.__class__.LAST_IN)
        self.cache_data[key] = item
        self.__class__.LAST_IN = key

    def get(self, key):
        '''Get an item by key'''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
