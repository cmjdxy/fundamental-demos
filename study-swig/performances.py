# -*- coding: utf-8 -*-
"""
A new file.
"""
import time
from functools import wraps
from numba import jit, vectorize

from example import factorial
from utils import add, sub, mul, div
from loops import loop1


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print('\nrun %s...' % func.__name__)
        t = time.clock()
        r = func(*args, **kw)
        print('time consumed: %.4fs' % (time.clock() - t))
        return r
    return wrapper


@timeit
def pyloop(n1, n2):
    s = 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            s += 1.0 / i + 1.0 / j
    return s


@timeit
@jit
def pyloop_jit(n1, n2):
    s = 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            s += 1.0 / i + 1.0 / j
    return s


@timeit
@vectorize('float64(int64, int64)')
def pyloop_vec(n1, n2):
    s = 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            s += 1.0 / i + 1.0 / j
    return s


@timeit
def cxxloop(n1, n2):
    return loop1(n1, n2)


@timeit
@jit
def cxxloop_jit(n1, n2):
    return loop1(n1, n2)


@timeit
@vectorize('float64(int64, int64)')
def cxxloop_vec(n1, n2):
    return loop1(n1, n2)


def main():
    n1 = 1000
    n2 = 1000

    a1 = pyloop(n1, n2)
    a1_jit = pyloop_jit(n1, n2)
    a1_vec = pyloop_vec(n1, n2)

    a2 = cxxloop(n1, n2)
    a2_jit = cxxloop_jit(n1, n2)
    a2_vec = cxxloop_vec(n1, n2)


if __name__ == '__main__':
    print('running...')
    main()
