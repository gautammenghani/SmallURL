import pytest
from SmallURL.helperFunctions import *

def test_isURLValid():
    result = isURLValid('https://google.com')
    assert(result == True)
    result = isURLValid('http://google.com')
    assert(result == True)
    result = isURLValid('https://google.com/result')
    assert(result == True)
    result = isURLValid('http://google.com/result')
    assert(result == True)
    result = isURLValid('http://')
    assert(result == False)
    result = isURLValid('random_text')
    assert(result == False)

def test_hashURL():
    result = hashURL('https://google.com')
    assert result == '05046f2'

def test_getFromCache():
    result = getFromCache('https://abcd.com')
    assert result == False

    result = getFromCache('https://google.com')
    assert result != False

def test_setCache():
    result = setCache('1180493', 'https://pqr.com')
    assert result != False
