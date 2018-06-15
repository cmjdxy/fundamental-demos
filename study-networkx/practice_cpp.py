# -*- coding: utf-8 -*-
"""
A new file.
"""
import matplotlib.pyplot as plt
import networkx as nx


# a quick example
g = nx.Graph()
g.add_weighted_edges_from([
    ('a', 'b', 0.1),
    ('b', 'c', 1.5),
    ('a', 'c', 1.0),
    ('c', 'd', 2.2)
])
print(nx.shortest_path(g, 'b', 'd')) # no weight
print(nx.shortest_path(g, 'b', 'd', weight='weight')) # with weight

# analysis






