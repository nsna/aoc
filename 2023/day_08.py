from utils import day
from itertools import cycle
import re
from math import lcm
import time

start_time = time.time()
LINES = day(8).splitlines()

def get_cycle():
    return cycle(map(int, list(LINES[0].translate(str.maketrans('LR', '01')))))

def get_nodes():
    nodes = {}
    for line in LINES[2:]:
        node, *edges = re.findall(r'\w+', line)
        nodes[node] = edges
    return nodes

def traverse(start, end):
    c = get_cycle()
    d = next(c)
    steps = 0
    node = start
    while not end(node):
        node = nodes[node][d]
        d = next(c)
        steps += 1
    return steps

def part1():
    print(traverse('AAA', lambda x: x == 'ZZZ'))

def part2():
    start_nodes = [node for node in nodes if node[-1] == 'A']
    steps_per_node = [traverse(node, lambda x: x[-1] == 'Z') for node in start_nodes]
    print(lcm(*steps_per_node))

nodes = get_nodes()
part1()
part2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))