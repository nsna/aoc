from collections import defaultdict
from itertools import combinations

from utils import day

GRID = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()
GRID = day(8).splitlines()

def parse():
    y, x, antennas = 0, 0, defaultdict(list)
    for y, col in enumerate(GRID):
        for x, row in enumerate(col):
            if GRID[y][x] != '.':
                antennas[GRID[y][x]].append((y, x))
    return y, x, antennas

HEIGHT, WIDTH, ANTENNAS = parse()

def p1():
    antinodes = set([])
    for freq in ANTENNAS:
        for (y1, x1), (y2, x2) in combinations(ANTENNAS[freq], 2):
            dy = y2 - y1
            dx = x2 - x1
            potential = [(y2 + dy, x2 + dx), (y1 - dy, x1 - dx)]
            for (y, x) in potential:
                if (0 <= y <= HEIGHT and 0 <= x <= WIDTH):
                    antinodes.add((y, x))
    print(len(antinodes))

def flatten(inp):
    return [x for lst in inp for x in lst]

def p2():
    antinodes = set([])
    for freq in ANTENNAS:
        for (y1, x1), (y2, x2) in combinations(ANTENNAS[freq], 2):
            dy = y2 - y1
            dx = x2 - x1
            potential = []
            for i in range(1, 50):
                potential.append((y2 + i * dy, x2 + i * dx))
                potential.append((y1 - i * dy, x1 - i * dx))
            for (y, x) in potential:
                if (0 <= y <= HEIGHT and 0 <= x <= WIDTH):
                    antinodes.add((y, x))
    antinodes |= set(flatten(ANTENNAS.values()))
    print(len(antinodes))

p1()
p2()
