# -*- coding: utf-8 -*-
"""
A new file.
"""
import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print('\nrun %s...' % func.__name__)
        t = time.clock()
        r = func(*args, **kw)
        print('time consumed: %.4fs' % (time.clock() - t))
        return r
    return wrapper

