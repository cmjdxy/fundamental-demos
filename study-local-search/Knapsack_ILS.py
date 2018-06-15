# -*- coding: utf-8 -*-
"""
Iterated Local Search.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
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


def main():
    '''main interface'''
    instance_number = 200
    max_capacity = 112648
    data = read_dataset()
    weights = data['weight'].as_matrix().tolist()
    values = data['value'].as_matrix().tolist()

    best_value = 0
    num_inter = 1000 #how many random points we use to initially use for search
    n_flip = 2
    lst_best_value = []
    items_selected = list(map(int, binrep(random.randint(0, 2**instance_number-1), instance_number)))
    # change '1010' to [1, 0, 1, 0], representing combination in bit-mode
    while num_inter > 0:
        max_eval = 1000
        for i in range(0, n_flip):
            idx = random.randint(0, instance_number-1)
            items_selected[idx] = 1 - items_selected[idx] # like mutation
        while max_eval > 0:
            total_value = np.dot(values, items_selected)
            total_weight = np.dot(weights, items_selected)
            if total_weight <= max_capacity:
                if total_value > best_value:
                    best_value = total_value
                    lst_best_value.append(best_value)
            max_eval -=1
        num_inter -= 1
    print(lst_best_value)
    print("best value = ",max(lst_best_value))

    plt.plot(list(range(0, len(lst_best_value))), lst_best_value)
    plt.show()


if __name__ == '__main__':
    print('running...')
    main()
#result: 131998
