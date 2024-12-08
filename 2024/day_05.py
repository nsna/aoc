from collections import defaultdict
from graphlib import TopologicalSorter

from utils import day

RAW = day(5)

def parse():
    rules, updates = RAW.split('\n\n')
    graph = defaultdict(list)
    for a, b in (rule.split('|') for rule in rules.splitlines()):
        graph[int(a)].append(int(b))
    updates = [
        [int(n) for n in update]
        for update in [update.split(',') for update in updates.splitlines()]
    ]
    return graph, updates

GRAPH, UPDATES = parse()
OUT_OF_ORDER = []

def get_subgraph(update):
    return defaultdict(list, {
        key: [value for value in GRAPH[key] if value in update]
        for key in GRAPH if key in update
    })

def p1():
    page_sum = 0
    for update in UPDATES:
        graph = get_subgraph(update)
        if all(b in graph[a] for (a, b) in zip(update, update[1:])):
            page_sum += update[len(update) // 2]
        else:
            OUT_OF_ORDER.append(update)
    print(page_sum)

def p2():
    page_sum = 0
    for update in OUT_OF_ORDER:
        graph = get_subgraph(update)
        sorted = tuple(TopologicalSorter(graph).static_order())
        page_sum += sorted[len(sorted) // 2]
    print(page_sum)

# manual DFS
#def p2():
#    # topological sort of graph using DFS
#    page_sum = 0
#    for update in OUT_OF_ORDER:
#        # get a subset of the graph
#        graph = get_subgraph(update)
#        visited = set([])
#        stack = []
#
#        def dfs(node):
#            if node in visited:
#                return
#            visited.add(node)
#            for neighbour in graph[node]:
#                if neighbour in update:
#                    dfs(neighbour)
#            stack.append(node)
#
#        for node in update:
#            if node not in visited:
#                dfs(node)
#
#        page_sum += stack[len(stack) // 2]
#    print(page_sum)

p1()
p2()
