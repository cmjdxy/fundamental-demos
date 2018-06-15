# -*- coding: utf-8 -*-
"""
A new file.
"""
import random


def shuffle(index):
    index_copy = index.copy()
    random.shuffle(index_copy)
    return index_copy


def main():
    index = list(range(3))
    indexs = []
    for i in range(9):
        index2 = shuffle(index)
        indexs.append(index2)


if __name__ == '__main__':
    print('running...')
#    main()
