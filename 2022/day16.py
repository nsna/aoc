# moving rooms takes 1 minute
# opening valve takes 1 minute
# find shortest most expensive route
import networkx as nx
import re
import heapq

RAW = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

def parse():
    paths = nx.DiGraph()
    costs = {}
    for line in RAW.splitlines():
        valve, flow, *edges = re.findall(r'(\d{1,2}|[A-Z]{2})', line)
        # only consider valves with non-zero flowrate
        if flow != "0":
            costs[valve] = int(flow)
        for edge in edges:
            paths.add_edge(valve, edge)
            
    return dict(nx.all_pairs_shortest_path_length(paths)), costs

def dfs():
    pass

paths, costs = parse()
print(paths)
print(costs)

#nx.draw(valves, with_labels=True, font_weight='bold')
#plt.savefig("graph.png")