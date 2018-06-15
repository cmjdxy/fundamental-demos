# -*- coding: utf-8 -*-
"""
Dynamic Programming.
"""
import pandas as pd
from smart_open import smart_open


def read_dataset():
    '''function to read dataset from file'''
    file = './data/hard200.txt'
    with smart_open(file, 'r') as f:
        lines = f.readlines()
    data = [list(map(int, line.split())) for line in lines]
    data = pd.DataFrame(data, columns=['no', 'value', 'weight'])
    return data


def binrep(n, r):
    '''represent n in r-length bit mode'''
    return "{0:0{1}b}".format(n, r)


def dp_table(weights, values, n_item, max_vol):
    '''dynamic programming fill in the table'''
    table = [[0 for j in range(max_vol+1)] for i in range(n_item+1)]

    for i in range(1, n_item+1):
        for w in range(1, max_vol+1):
            if weights[i-1] > w:
                table[i][w] = table[i-1][w]
            else:
                table[i][w] = max(table[i-1][w], values[i-1]+table[i-1][w-weights[i-1]])
    return table


def dp_path(weights, n_item, max_vol, table):
    '''find path in table backwards'''
    path = [0] * n_item
    j = max_vol
    for i in reversed(range(1, n_item+1)):
        if table[i][j] != table[i-1][j]:
            path[i-1] = 1
            j -= weights[i-1]
    index = []
    for i, p in enumerate(path):
        if p > 0:
            index.append(i)
    return index


def run():
    '''main interface'''
    n_item = 200
    max_vol = 112648
    data = read_dataset()
    weights = data['weight'].as_matrix()#.tolist()
    values = data['value'].as_matrix()#.tolist()

    sol_table = dp_table(weights, values, n_item, max_vol)
    sol_path = dp_path(weights, n_item, max_vol, sol_table)
    print('best value:', sol_table[-1][-1])
    print('combination:', sol_path)


def test():
    values = [1, 6, 18, 22, 28]
    weights = [1, 2, 5, 6, 7]
    n_item = 5
    max_vol = 11

    sol_table = dp_table(weights, values, n_item, max_vol)
    sol_path = dp_path(weights, n_item, max_vol, sol_table)
    print('best value:', sol_table[-1][-1])
    print('combination:', sol_path)


if __name__ == '__main__':
    print('running...')
    run()
#result: 137448