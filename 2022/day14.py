from itertools import pairwise
from math import copysign

from utils import ints, day
from more_itertools import chunked

RAW = day(14)
#RAW = """498,4 -> 498,6 -> 496,6
#503,4 -> 502,4 -> 502,9 -> 494,9"""

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
    return cave

cave = parse()

def part1():
    floor = max([y for x, y in cave])
    while True:
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

def part2():
    floor = max([y for x, y in cave]) + 2
    while cave[500, 0] != SAND:
        x = 500
        for y in range(floor):
            if y + 1 == floor:
                cave[x, y] = SAND
                break
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
            break
        
    print(sum(value == SAND for value in cave.values()))

part1()
part2()