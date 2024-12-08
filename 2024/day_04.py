from collections import defaultdict
from utils import day

RAW = day(4)

GRID = RAW.splitlines()
DIRS = {
    (0, 1): False,
    (0, -1): False,
    (1, 0): False,
    (-1, 0): False,
    (1, 1): False,
    (-1, -1): False,
    (1, -1): False,
    (-1, 1): False
}
HEIGHT = len(GRID)
WIDTH = len(GRID[0])

def in_bounds(y, x):
    return 0 <= y < HEIGHT and 0 <= x < WIDTH

def check(y, x):
    # return the number of found XMAS from (y, x) coordinate
    if GRID[y][x] != 'X':
        return 0
    # reset directions
    for (dy, dx) in DIRS:
        DIRS[(dy, dx)] = True
    # check remaining characters
    for distance, char in enumerate('MAS', start=1):
        for (dy, dx) in [direction for direction in DIRS if DIRS[direction]]:
            yi = y + (distance * dy)
            xi = x + (distance * dx)
            if not in_bounds(yi, xi):
                DIRS[(dy, dx)] = False
                continue
            DIRS[(dy, dx)] = (GRID[yi][xi] == char)
    # count good
    return sum(DIRS.values())

def p1():
    print(sum(check(y, x) for y in range(HEIGHT) for x in range(WIDTH)))

def p2():
    opposing = defaultdict(str, {'M': 'S', 'S': 'M'})
    s = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if GRID[y][x] != 'A':
                continue
            if not (in_bounds(y - 1, x - 1) and in_bounds(y + 1, x + 1)):
                continue
            s += (
                opposing[GRID[y-1][x-1]] == GRID[y+1][x+1]
                and
                opposing[GRID[y-1][x+1]] == GRID[y+1][x-1]
            )
    print(s)

p1()
p2()
