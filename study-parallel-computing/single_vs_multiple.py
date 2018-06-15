# -*- coding: utf-8 -*-
"""
A new file.
"""
import argparse
from functools import partial
from joblib import delayed, Parallel

from utils import timeit


def func(x, y):
    return x + y, x**2 + y**2


@timeit
def multiple(args):
    func2 = partial(func, 10)
    parallel = Parallel(n_jobs=args.n_jobs)
    result = parallel(delayed(func2)(i) for i in range(args.range))
    print(result)
    return result


@timeit
def single(args):
    result = []
    for i in range(args.range):
        for j in range(args.range):
            result.append(func(i, j))
    print(result)
    return result


def main():
    parser = argparse.ArgumentParser(description='Parallel by joblib')
    parser.add_argument('--n_jobs', type=int, default=2)
    parser.add_argument('--range', type=int, default=10)
    args = parser.parse_args()

    multiple(args)
#    single(args)


if __name__ == '__main__':
    print('running...')
    main()

