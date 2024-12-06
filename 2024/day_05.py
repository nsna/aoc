from collections import defaultdict
from math import ceil

from utils import day

RAW = day(5)

rules, updates = RAW.split('\n\n')
GRAPH = defaultdict(list)
for a, b in (rule.split('|') for rule in rules.splitlines()):
    GRAPH[int(a)].append(int(b))

UPDATES = [[int(n) for n in update] for update in [update.split(',') for update in updates.splitlines()]]
OUT_OF_ORDER = []

def p1():
    page_sum = 0
    for update in UPDATES:
        valid = True
        for a, b in zip(update, update[1:]):
            if b not in GRAPH[a]:
                valid = False
                OUT_OF_ORDER.append(update)
                break
        if valid:
            page_sum += update[ceil(len(update) / 2) - 1]
    print(page_sum)

def p2():
    # topological sort of graph using DFS
    page_sum = 0
    for update in OUT_OF_ORDER:
        visited = set([])
        stack = []

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in GRAPH[node]:
                if neighbour in update:
                    dfs(neighbour)
            stack.append(node)

        for node in update:
            if node not in visited:
                dfs(node)

        page_sum += stack[ceil(len(stack) / 2) - 1]
    print(page_sum)

p1()
p2()
