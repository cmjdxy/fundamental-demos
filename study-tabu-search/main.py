# -*- coding: utf-8 -*-
"""
A new file.
"""
import argparse
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

from utils import (
    get_neighbors_and_rules,
    distance,
    shuffle,
    swap,
    sort
)

plt.style.use('seaborn')


class TabuSearch:
    '''
    a class for tabu search.
    '''
    def __init__(self, tabu_size, distance_matrix):
        self.tabu_size = tabu_size
        self.distance_matrix = distance_matrix
    def evolve(self, init, max_gen, k_opt=2):
        x = init
        gen = 0
        tabu_list = [0] * self.tabu_size
        while gen < max_gen:
            print('gen %d...' % gen, end='')
            x_neighbors, rules = get_neighbors_and_rules(x, k_opt) # 2-opt is usually better
            dists = list(map(lambda x : distance(self.distance_matrix, x), x_neighbors))
            sorted_dists, sorted_index = sort(dists)
            min_dist = sorted_dists[0]
            min_id = sorted_index[0]
            min_rule = rules[min_id]
            if min_dist < distance(self.distance_matrix, x): # aspiration
                # update tabu list
                tabu_list.insert(0, min_rule)
                tabu_list.pop()
                x = swap(x, min_rule)
            else:
                while min_rule in tabu_list:
                    sorted_index.pop(0)
                    min_id = sorted_index[0]
                    min_rule = rules[min_id]
                # update tabu list
                tabu_list.insert(0, min_rule)
                tabu_list.pop()
                x = swap(x, min_rule)
            gen += 1
            print('done!')
        return tabu_list, x, distance(self.distance_matrix, x)
    def run(self, n_inits, max_gen):
        inits = self._get_inits(n_inits)
        opt_solus = []
        opt_dists = []
        for init in inits:
            _, opt_x, opt_d = self.evolve(init, max_gen)
            opt_solus.append(opt_x)
            opt_dists.append(opt_d)
        min_dist = min(opt_dists)
        min_id = opt_dists.index(min_dist)
        min_solu = opt_solus[min_id]
        print('optimal solution:', min_solu)
        print('optimal distance:', min_dist)
        return min_solu, min_dist
    def _get_inits(self, n_inits):
        init = list(range(len(self.distance_matrix)))
        inits = []
        for i in range(n_inits):
            new_init = shuffle(init)
            inits.append(new_init)
        return inits


def test1(args):
    '''
    a classical example.
    '''
    distance_matrix = pd.read_csv('tsp-01.csv', header=None).as_matrix().tolist()

    ts = TabuSearch(args.tabu_size, distance_matrix)
    t = time.clock()
    ts.run(args.n_inits, args.max_gen)
    print('time consumed: %.2fs' % (time.clock() - t))


def test2(args):
    '''
    TSP for att48.
    '''
    with open('att48.txt', 'r') as f:
        lines = f.readlines()
    nodes = []
    for line in lines:
        nodes.append([int(line.split()[1]), int(line.split()[2])])

    D = np.zeros([48, 48], dtype=np.int32)
    for i1, node1 in enumerate(nodes):
        for i2, node2 in enumerate(nodes):
            x1, y1 = node1
            x2, y2 = node2
            D[i1, i2] = math.ceil(math.sqrt(((x1 - x2)**2 + (y1 - y2)**2) / 10))

    ts = TabuSearch(args.tabu_size, D)
    t = time.clock()
    ts.run(args.n_inits, args.max_gen)
    print('time consumed: %.2fs' % (time.clock() - t))

def main():
    parser = argparse.ArgumentParser(description='Tabu Search for TSP')
    parser.add_argument('--tabu_size', type=int, default=5,
    help='size of tabu list.')
    parser.add_argument('--max_gen', type=int, default=100,
    help='number of maximal generation.')
    parser.add_argument('--n_inits', type=int, default=10,
    help='number of initial solutions.')
    args = parser.parse_args()

    test2(args)


if __name__ == '__main__':
    print('running...')
    main()
