# -*- coding: utf-8 -*-
"""
A new file.
"""
import networkx as nx
from sys import getsizeof


# nodes
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_node(H)

# edges
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)
G.add_edges_from([(1, 2), (1, 3)])
G.add_edges_from(H.edges)
G.clear()

G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node('spam') # add 'spam'
G.add_nodes_from('spam') # add 's', 'p', 'a', 'm'
G.add_edge(3, 'm')
list(G.adj[1])
G.degree[1]
G.edges([1, 2]) # edges linked to 1, 2
G.degree([1, 2]) # degrees of 1, 2

G.remove_node(1)
G.remove_nodes_from('spam') # remove 's', 'p', 'a', 'm'
G.nodes
G.edges
G.add_edge(1, 2)
H = nx.DiGraph(G) # Directed graph
H.edges()
edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist)

# accessing
G[2] # G.adj[2], G.neighbors(2)
G[1][2] # weight on (1, 2)
G.edges[1, 2] # weight on (1, 2)

G.add_edge(1, 3)
G[1][3]['color'] = "blue"
G.edges[1, 2]['color'] = "red"
list(G.adjacency()) # all (node, adjacency) pairs, same below
list(G.adj.item())

FG = nx.Graph()
FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
for n, nbrs in FG.adj.items():
    print(n, nbrs)

# adding attributes
G = nx.Graph(day="Friday")
G.graph

G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')
G.nodes[1]
G.nodes[1]['room'] = 714
 # show all (node, key, value) triplets

G.add_edge(1, 2, weight=4.7)
G.add_edges_from([(3, 4), (4, 5)], color='red')
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
G[1][2]['weight']
G.edges[3, 4]['weight'] = 4.2
G.edges.data()

# Directed graphs
DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
DG.add_edge(2, 1, weight=0.25) # will override the previous value when converting to undirected graph
DG.out_degree(1, weight='weight')
DG.degree(1, weight='weight')
list(DG.predecessors(1)) # pointed
list(DG.successors(1)) # pointing
list(DG.neighbors(1)) # pointing
H = DG.to_undirected()
H = nx.Graph(G)

# Multigraphs
MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])
dict(MG.degree(weight='weight'))

GG = nx.Graph()
for n, nbrs in MG.adjacency():
   for nbr, edict in nbrs.items():
       minvalue = min([d['weight'] for d in edict.values()])
       GG.add_edge(n, nbr, weight = minvalue)
nx.shortest_path(GG, 1, 3)

# generators and operations
petersen = nx.petersen_graph()
tutte = nx.tutte_graph()
maze = nx.sedgewick_maze_graph()
tet = nx.tetrahedral_graph()
K_5 = nx.complete_graph(5)
K_3_5 = nx.complete_bipartite_graph(3, 5)
barbell = nx.barbell_graph(10, 10)
lollipop = nx.lollipop_graph(10, 20)
er = nx.erdos_renyi_graph(100, 0.15)
ws = nx.watts_strogatz_graph(30, 3, 0.1)
ba = nx.barabasi_albert_graph(100, 5)
red = nx.random_lobster(100, 0.9, 0.9)

# analyzing
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3)])
G.add_node("spam")       # adds node "spam"
list(nx.connected_components(G))
sorted(d for n, d in G.degree())
nx.clustering(G)
sp = dict(nx.all_pairs_shortest_path(G))
sp[3]

# drawing
import matplotlib.pyplot as plt

plt.figure(0)
plt.subplot(221)
nx.draw(petersen, with_labels=True)
plt.subplot(222)
nx.draw(tutte, with_labels=True)
plt.subplot(223)
nx.draw(maze, with_labels=True)
plt.subplot(224)
nx.draw(tet, with_labels=True)

options = {
    'node_color': 'blue',
    'node_size': 50,
    'width': 1,
}
plt.subplot(221)
nx.draw_random(G, **options)
plt.subplot(222)
nx.draw_circular(G, **options)
plt.subplot(223)
nx.draw_spectral(G, **options)
plt.subplot(224)
nx.draw_shell(G, nlist=[range(5,10), range(5)], **options)
