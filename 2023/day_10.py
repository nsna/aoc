from utils import day
from operator import add
import time

start_time = time.time()
GRID = day(10).splitlines()

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)

def parse():
    pipes = {
        '|': {N: N, S: S},
        '-': {W: W, E: E},
        'L': {S: E, W: N},
        'J': {E: N, S: W},
        '7': {N: W, E: S},
        'F': {N: E, W: S}
    }
    steps = [(y, x) for y in range(len(GRID)) for x in range(len(GRID[y])) if GRID[y][x] == "S"]
    start = pos = steps[0]
    dir = S
    pos = tuple(map(add, pos, dir))
    while pos != start:
        steps.append(pos)
        y, x = pos
        pipe = GRID[y][x]
        dir = pipes[pipe][dir]
        pos = tuple(map(add, pos, dir))
    return steps

def part1():
    print(len(loop) / 2)

def part2():
    # shoelace theorem
    a = 0
    b = 0
    for i in range(len(loop)):
        a += loop[i][1] * loop[(i + 1) % len(loop)][0]
        b += loop[i][0] * loop[(i + 1) % len(loop)][1]
    total_area = abs(a - b) / 2
    # approximation
    intersecting_with_edges = (len(loop) / 2) - 1
    print(total_area - intersecting_with_edges)

loop = parse()
part1()
part2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))