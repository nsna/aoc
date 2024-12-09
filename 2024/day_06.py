from operator import add
from collections import defaultdict

from utils import day

GRID = day(6).splitlines()
HEIGHT = len(GRID)
WIDTH = len(GRID[0])

def parse():
    obstacles = []
    guard = (0, 0)
    for y, line in enumerate(GRID):
        for x, char in enumerate(line):
            if char == '#':
                obstacles.append((y, x))
            elif char == '^':
                guard = (y, x)
    return obstacles, guard

OBSTACLES, GUARD = parse()

def rotate(y, x):
    return x, -y

def march(direction, guard, obstacles):
    visited = defaultdict(list)
    condition = ''
    while True:
        y, x = map(add, guard, direction)
        if not (0 <= y < HEIGHT and 0 <= x < WIDTH):
            condition = 'complete'
            break
        if (y, x) in obstacles:
            direction = rotate(*direction)
        elif direction in visited[(y, x)]:
            condition = 'loop'
            break
        else:
            guard = (y, x)
            visited[(y, x)].append(direction)
    return condition, visited

def p1():
    condition, path = march((-1, 0), GUARD, OBSTACLES)
    print(len(path))

def p2():
    condition, path = march((-1, 0), GUARD, OBSTACLES)
    path.pop(GUARD)
    loops = 0
    for node in path:
        condition, path = march((-1, 0), GUARD, OBSTACLES + [node])
        if condition == 'loop':
            loops += 1
    print(loops)

p1()
p2()
