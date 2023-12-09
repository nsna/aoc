from utils import day
from itertools import cycle
import re
from math import lcm
import time

start_time = time.time()
LINES = day(8).splitlines()

def instructions():
    return cycle(map(int, list(LINES[0].translate(str.maketrans('LR', '01')))))

def get_nodes():
    nodes = {}
    for line in LINES[2:]:
        node, *edges = re.findall(r'\w+', line)
        nodes[node] = edges
    return nodes

def traverse(start, end):
    node = start
    for steps, direction in enumerate(instructions()):
        node = nodes[node][direction]
        if end(node):
            return steps + 1

def part1():
    print(traverse('AAA', lambda node: node == 'ZZZ'))

def part2():
    steps_per_node = (
        traverse(node, lambda node: node[-1] == 'Z') for node in nodes
        if node[-1] == ('A')
    )
    print(lcm(*steps_per_node))

nodes = get_nodes()
part1()
part2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))