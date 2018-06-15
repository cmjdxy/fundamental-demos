# -*- coding: utf-8 -*-
"""
A new file.
"""
from sys import getsizeof
import matplotlib.pyplot as plt
import numpy as np
import time

plt.style.use('seaborn')

# 1.vectorize
def func(x):
    x = x + 1
    y = 2 * x
    return y

def draw():
    x = np.linspace(-2, 2, 201)
    y = np.array(list(map(func, x)))
    plt.figure()
    plt.plot(x, y)
    plt.show()

def test1():
    x = np.linspace(-2, 2, 201)
    vfunc = np.vectorize(func)
    y = vfunc(x)
    plt.plot(x, y, 'r-')

# 2.piecewise
def test2():
    x = np.linspace(-2, 2, 201)
    y = np.piecewise(x,
                     [x < -1, (x >= -1) & (x <= 1), x > 1],
                     [lambda x: -2 * x -3,
                      lambda x: x,
                      lambda x: -2 * x + 3])
    plt.plot(x, y, 'm-')

def loop():
    t = time.clock()
    s = 0
    for i in range(1, 10001):
        for j in range(1, 100001):
            s += 1 / i + 1 / j
    print('sum is: {0}, time consumed: {1}s'.format(s, (time.clock() - t)))

def sum_up():
    s = 0
    for i in range(50, 101):
        s += i
    print('50到100的总和: {0}'.format(s))



if __name__ == '__main__':
    print('running...')
    sum_up()
