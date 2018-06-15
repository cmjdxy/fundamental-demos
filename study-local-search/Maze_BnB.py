# -*- coding: utf-8 -*-
"""
source -- https://www.2cto.com/kf/201402/278689.html
"""
import networkx as nx
import numpy as np
import random


def evolve(g, entry, direction):
    update_position = {
        'a' : (entry[0], entry[1]-1),
        'd' : (entry[0], entry[1]+1),
        'w' : (entry[0]-1, entry[1]),
        's' : (entry[0]+1, entry[1])
    }
    new_entry = update_position[direction]
    # check legality
    if new_entry not in g.node or g.node[new_entry]['mark'] == -1:
        return g, entry
    else:
        if g.node[new_entry]['mark'] == 0: # unreached position
            g.node[new_entry]['mark'] = 1
            g.node[new_entry]['path'] = g.node[entry]['path'] + [direction]
            g.node[new_entry]['step'] = g.node[entry]['step'] + 1
        else:
            if g.node[new_entry]['step'] > g.node[entry]['step'] + 1:
                g.node[new_entry]['path'] = g.node[entry]['path'] + [direction]
                g.node[new_entry]['step'] = g.node[entry]['step'] + 1
        return g, new_entry


'''
better paradigm:
1.update d;
2.reverse d to rd.
because update rd would search rd.values() by rd.keys()
'''
def reverse_dict(d):
    rd = {}
    for v in d.values():
        rd[v] = []
    for k, v in d.items():
        rd[v].append(k)
    return rd


def main():
    # data
    grids = [[ 0,  0, -1,  0,  0,  0,  0],
             [ 0,  0, -1, -1,  0,  0,  0],
             [ 0,  0,  0,  0, -1,  0,  0],
             [ 0,  0,  0, -1, -1,  0,  0],
             [-1,  0,  0,  0, -1,  0,  0],
             [-1, -1, -1,  0,  0,  0,  0],
             [-1, -1, -1,  0,  0,  0,  0]]
    directions = ['a', 'd', 'w', 's']
    entry_init = (2, 1)
    entry_term = (3, 5)
    hash_table = {entry_init : 0} # {entry: step}
    reverse_hash_table = reverse_dict(hash_table)
    g = nx.Graph()
    for i, j in np.ndindex(7, 7):
        g.add_node((i, j), mark=grids[i][j], path=[], step=0)
    g.node[entry_init]['mark'] = 1
    # loop
    level = 0
    while g.node[entry_term]['mark'] != 1:
        entries = reverse_hash_table[level]
        for entry in entries:
            random.shuffle(directions)
            for direction in directions:
                g, new_entry = evolve(g, entry, direction)
                hash_table.update({new_entry : g.node[new_entry]['step']})
        reverse_hash_table = reverse_dict(hash_table)
        level += 1
    print(g.node[entry_term])


if __name__ == '__main__':
    print('running...')
    main()
