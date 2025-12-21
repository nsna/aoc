import networkx as nx
from utils import day

RAW = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
# RAW = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out
# """
# RAW = day(11)


def parse():
    return {
        node[:-1]: edges for line in RAW.splitlines() for node, *edges in [line.split()]
    }


G = nx.DiGraph(parse())
print(len(list(nx.all_simple_paths(G, "you", "out"))))

# print(len(list(nx.all_simple_paths(G, "svr", "out"))))
