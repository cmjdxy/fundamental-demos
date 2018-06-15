# -*- coding: utf-8 -*-
"""
A new file.
"""
import os
from multiprocessing import Pool, Process

from utils import timeit


def func(x):
    return x**2


# *** Pool *** #
'''
data parallel
'''
@timeit
def test1_multi():
    with Pool(processes=2) as pool:
        print(pool.map(func, range(100)))
@timeit
def test1_uni():
    print(list(map(func, range(100))))


# *** Process *** #
'''
start a process
'''
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def greet(name):
    print('hello, %s!' % name)


def test2():
    info('main line')
    p = Process(target=greet, args=('Bob',))
    p.start()
    p.join()






def main():
    # 多进程不如单进程
#    test1_uni()
#    test1_multi()

    test2()


if __name__ == '__main__':
    print('running...')
    main()
