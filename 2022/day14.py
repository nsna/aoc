from itertools import pairwise
from math import copysign

from utils import ints, day
from more_itertools import chunked

#RAW = day(14)
RAW = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
#488,11 -> 514,11"""

VOID = 0
ROCK = 1
SAND = 2

# need dict to handle unknown indexes
# defaultdict inserts on missing key which is not what we want
# so we will create our own.
class CaveDict(dict):
    def __missing__(self, key):
        # I want a missing key to return a false-y value
        return VOID
        
def parse():
    cave = CaveDict()
    for wall in RAW.splitlines():
        for (x1, y1), (x2, y2) in pairwise(chunked(ints(wall), 2)):
            dir_x = int(copysign(1, x2 - x1))
            dir_y = int(copysign(1, y2 - y1))
            for x in range(x1, x2 + (1 * dir_x), dir_x):
                for y in range(y1, y2 + (1 * dir_y), dir_y):
                    cave[x, y] = ROCK
    cave.floor = max([y for x, y in cave]) + 2
    return cave

cave = parse()
print(cave.floor)

def fill_sand(floor):
    print(floor)
    while cave[500, 0] != SAND:
        x = 500
        for y in range(floor):
            if cave[x, y + 1] == VOID:
                x += 0
            elif cave[x - 1, y + 1] == VOID:
                x += -1
            elif cave[x + 1, y + 1] == VOID:
                x += 1
            else:
                cave[x, y] = SAND
                break
        else:
            # we didn't save a sand coordinate, so break out of
            # the infinite loop
            break
        
    print(sum(value == SAND for value in cave.values()))

def print_cave():
    min_x = min(key[0] for key in cave.keys())
    max_x = max(key[0] for key in cave.keys())
    min_y = min(key[1] for key in cave.keys())
    max_y = max(key[1] for key in cave.keys())

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = [['.' for _ in range(width)] for _ in range(height)]
    for (x, y), value in cave.items():
        if value == 1:
            grid[y - min_y][x - min_x] = '#'
        elif value == 2:
            grid[y - min_y][x - min_x] = 'o'
    
    for row in grid:
        print(''.join(row))

#day1
floor = max([y for x, y in cave])
print('part1')
fill_sand(floor - 2)
print_cave()
#day2()
print('part2')
fill_sand(floor)
print_cave()