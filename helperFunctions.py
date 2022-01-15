import re
import hashlib

def isURLValid(url):
    regex = re.compile('^http(s)?:\/\/[a-zA-Z]+.[a-zA-Z\/.]*')
    if len(url)>0 and regex.match(url)!=None:
        return True
    else:
        return False

def hashURL(url):
    result = hashlib.sha256(url.encode())
    return result.hexdigest()[0:7]
