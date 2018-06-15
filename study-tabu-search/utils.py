# -*- coding: utf-8 -*-
"""
A new file.
"""
from functools import wraps
from itertools import permutations, combinations
import numpy as np
import time


# ======= decorator ======= #
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print('\nrun %s...' % func.__name__)
        t = time.clock()
        r = func(*args, **kw)
        print('time consumed: %.4fs' % (time.clock() - t))
        return r
    return wrapper


# ======= main interface ======= #
def get_neighbors_and_rules(elements, k):
    '''
    swap k points of elements, return all possible neighbors and the rules.
    '''
    neighbors = []
    rules = []
    for comb in combinations(range(len(elements)), k):
        rot_indices = _rotate(list(comb))
        for rot_index in rot_indices:
            neighbors.append(_swap(elements, rot_index))
            rules.extend(unify_rule(rot_index)) # unify permutations
    return neighbors, rules


def distance(D, x):
    '''
    distance function.
    '''
    s = 0
    lshift_x = x[1:] + [x[0]]
    for i, li in zip(x, lshift_x):
        s += D[i][li]
    return s


def shuffle(index):
    '''
    shuffle index and return it.
    '''
    index_copy = index.copy()
    np.random.shuffle(index_copy)
    return index_copy


def swap(elements, rot_index):
    '''
    swap elements according to rot_index.
    '''
    return _swap(elements, rot_index)


def unify_rule(index):
    '''
    rule to swap.
    '''
    shift_index = _min_lshift(index)
    return _rotate(shift_index)


def sort(elements, reverse=False):
    '''
    sort elements in ascending order, return sorted elements and index.
    '''
    elements = list(elements)
    sorted_elements = np.sort(elements).tolist()
    sorted_index = np.argsort(elements).tolist()
    if reverse:
        sorted_elements = sorted_elements[::-1]
        sorted_index = sorted_index[::-1]
    return sorted_elements, sorted_index


# ======= sub functions ======= #
def _rotate(index):
    '''
    fix first index, permute others.
    '''
    index = list(index)
    if len(index) < 3:
        rot_indices = [index]
    else:
        rot_indices = []
        for p in permutations(index[1:]):
            rot_indices.append([index[0]] + list(p))
    return rot_indices


def _swap(elements, rot_index):
    '''
    swap elements according to rot_index.
    '''
    swap_elements = elements.copy()
    lshift_index = rot_index[1:] + [rot_index[0]]
    for i, li in zip(rot_index, lshift_index):
        swap_elements[li] = elements[i]
    return swap_elements


def _min_lshift(index):
    '''
    left shift till min to the left.
    '''
    min_id = index.index(min(index))
    shift_index = index[min_id:] + index[:min_id]
    return shift_index
