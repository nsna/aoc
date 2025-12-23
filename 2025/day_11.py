from itertools import pairwise, starmap
from math import prod

import networkx as nx
from utils import day

RAW = day(11)


def parse():
    return {
        node[:-1]: edges for line in RAW.splitlines() for node, *edges in [line.split()]
    }


G = nx.DiGraph(parse())
G_TOPO = list(nx.topological_sort(G))


def count_paths(source, target):
    # same approach as 2024 d5 p2
    counts = {node: 0 for node in G.nodes()}
    counts[target] = 1
    # Process nodes in reverse topological order
    for node in reversed(G_TOPO):
        for neighbor in G.successors(node):
            counts[node] += counts[neighbor]
    return counts[source]


def count_path_segments(source, target, *required):
    # sort the nodes according to their position in the graph's hierarchy
    s = [source, *sorted(required, key=G_TOPO.index), target]
    # return the product of the number of paths between each segment
    # Total=(Paths Source→A)×...×(Paths X→Target)
    return prod(starmap(count_paths, pairwise(s)))


print(count_paths("svr", "out"))
print(count_path_segments("svr", "out", "dac", "fft"))
