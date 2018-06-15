# -*- coding: utf-8 -*-
"""
A new file.
"""
import numpy as np
from numba import jit, vectorize

from utils import timeit
from loops import loop1


@timeit
def loop(m, n):
    s = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s += 1.0 / i + 1.0 / j
    return s


@timeit
def loopcxx(m, n):
    return loop1(m, n)


@timeit
@jit
def loop_jit(m, n):
    s = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s += 1.0 / i + 1.0 / j
    return s


@timeit
@vectorize(['float64(int64, int64)'])
def loop_vec(m, n):
    s = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s += 1.0 / i + 1.0 / j
    return s


def main():
    m = 10000
    n = 1000
    r = loop(m, n)
    r1 = loopcxx(m, n)
    r_jit = loop_jit(m, n)
    r_vec = loop_vec(m, n)
    print(r, r1, r_jit, r_vec)


if __name__ == '__main__':
    print('running...')
    main()
