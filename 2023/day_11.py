from utils import day
from itertools import combinations

SPACE = day(11).splitlines()

def parse(offset=1):
    # off by 1 error 🙄
    if offset > 1: offset -= 1
    width = len(SPACE[0])
    height = len(SPACE)
    empty_rows = [y for y in range(height) if not "#" in SPACE[y]]
    empty_cols = [x for x in range(width) if not "#" in (SPACE[y][x] for y in range(width))]
    galaxies = [(y, x) for y in range(width) for x in range(height) if SPACE[y][x] == "#"]

    while empty_cols:
        col = empty_cols.pop(0)
        empty_cols = [col + offset for col in empty_cols]
        galaxies = [(y, x + offset) if x > col else (y, x) for (y, x) in galaxies]

    while empty_rows:
        row = empty_rows.pop(0)
        empty_rows = [row + offset for row in empty_rows]
        galaxies = [(y + offset, x) if y > row else (y, x) for (y, x) in galaxies]

    return galaxies

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part1():
    print(sum((dist(a, b) for a, b in combinations(parse(), 2))))

def part2():
    print(sum((dist(a, b) for a, b in combinations(parse(1_000_000), 2))))

part1()
part2()