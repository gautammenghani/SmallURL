import re
import hashlib
from cache_handling import setCache, getFromCache

def isURLValid(url):
    regex = re.compile('^http(s)?:\/\/[a-zA-Z]+.[a-zA-Z\/.]*')
    if len(url)>0 and regex.match(url)!=None:
        return True
    else:
        return False

def hashURL(url):
    c = getFromCache(url)
    if(c is False):
        print(f'{url} not in  cache')
        result = hashlib.sha256(url.encode()).hexdigest()[0:7]
        res = setCache(result, url)
        if res is False:
            return 'error'
        else:
            return result
    else:
        print(f'{url} is in  cache')
        c = c.decode('utf-8')       
        return c
