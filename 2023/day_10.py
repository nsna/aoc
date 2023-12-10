from utils import day
from operator import add
from shapely.geometry import Polygon, Point

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
    points = []
    poly = Polygon(loop)
    for y in range(len(GRID)):
        for x in range(len(GRID[y])):
            if poly.contains(Point(y, x)):
                points.append((y, x))
    print(len(points))

loop = parse()
part1()
part2()