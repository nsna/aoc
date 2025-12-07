from collections import defaultdict, deque

from utils import day

RAW = day(7)


def parse(inp):
    splitters = []
    start = ()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            if inp[y][x] == "S":
                start = (y, x)
            if inp[y][x] == "^":
                splitters.append((y, x))
    return start, splitters


def march(origin, splitters):
    rays = deque([(1,) + origin])
    depth = 0
    max_depth = max(splitters)[0]
    visited_splitters = {splitter: 0 for splitter in splitters}
    while depth < max_depth:
        depth += 1
        new_rays = defaultdict(int)
        while rays:
            paths, y, x = rays.popleft()
            yi, xi = (y + 1), x
            if (yi, xi) in splitters:
                visited_splitters[(yi, xi)] += paths
                new_rays[(yi, x - 1)] += paths
                new_rays[(yi, x + 1)] += paths
            else:
                new_rays[(yi, xi)] += paths
        rays = deque([(paths, y, x) for (y, x), paths in new_rays.items()])
    return visited_splitters


start, splitters = parse(RAW.splitlines())
visited = march(start, splitters)
print(sum(val > 0 for val in visited.values()))
print(sum(val for val in visited.values()) + 1)
