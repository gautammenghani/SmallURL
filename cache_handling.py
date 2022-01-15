from pymemcache.client.base import Client
cache = Client('127.0.0.1:11211')

def getFromCache(url):
    rv = cache.get(url)
    if rv is None:
        return False
    else:
        return rv

def setCache(hash, url):
    rv = cache.set(url, hash)
    return rv
