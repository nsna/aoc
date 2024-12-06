from operator import add

from utils import day

GRID = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()
GRID = day(6).splitlines()

OBSTACLES = []
GUARD = (0, 0)
HEIGHT = len(GRID)
WIDTH = len(GRID[0])

for y, line in enumerate(GRID):
    for x, char in enumerate(line):
        if char == '#':
            OBSTACLES.append((y, x))
        elif char == '^':
            GUARD = (y, x)

VISITED = set([GUARD])
print(len(OBSTACLES))

def rotate(y, x):
    return x, -y

def p1():
    direction = (-1, 0)
    guard = GUARD
    while True:
        y, x = map(add, guard, direction)
        if not (0 <= y < HEIGHT and 0 <= x < WIDTH):
            break
        if (y, x) in OBSTACLES:
            direction = rotate(*direction)
        else:
            guard = (y, x)
            VISITED.add((y, x))
    print(len(VISITED))

def p2():
    ...

p1()
