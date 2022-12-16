from utils import day, delta4
import numpy as np
import networkx as nx

RAW = day(12)

def neighbours(y, x, height, width):
    # neighbours of x, y with boundary check
    deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for dy, dx in deltas:
        if 0 <= y + dy < height and 0 <= x + dx < width:
            yield (y + dy, x + dx)
    
def parse():
    grid = np.array(
        [[ord(c) for c in line] for line in RAW.split()]
    )
    # since the conditions say that only an increase of 1 is valid
    # set the origin and destination to 'a' (can fall without issue)
    origin = tuple(np.argwhere(grid == ord('S'))[0])
    grid[origin] = ord('a')
    destination = tuple(np.argwhere(grid == ord('E'))[0])
    grid[destination] = ord('z')
    # part2 - find all lowest elevation points
    lowest = map(tuple, np.argwhere(grid == ord('a')))
    
    # create directed (one-way) graph from the grid
    height, width = grid.shape
    graph = nx.DiGraph()
    for y in range(height):
        for x in range(width):
            for n in neighbours(y, x, height, width):
                if grid[n] - grid[(y, x)] <= 1:
                    graph.add_edge((y, x), n)
    
    return graph, origin, destination, lowest

graph, origin, destination, lowest = parse()

# part1
print(nx.shortest_path_length(graph, origin, destination))

# part2
lengths = []
for start in lowest:
    try:
        lengths.append(nx.shortest_path_length(graph, start, destination))
    except nx.NetworkXNoPath:
        pass

print(min(lengths))
