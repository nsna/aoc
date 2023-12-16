from utils import day
from itertools import chain

PATTERNS = [pattern.splitlines() for pattern in day(13).split('\n\n')]

def transpose(grid):
    return [*zip(*grid)]

def get_reflection(grid, smudged = 0):
    for i in range(1, len(grid)):
        left = grid[:i][::-1]
        right = grid[i:]

        edge = min(len(left), len(right))
        left = left[:edge]
        right = right[:edge]

        # element-wise comparison 
        if sum(l != r for l, r in zip(chain(*left), chain(*right))) == smudged:
            return i
    return 0

def part1():
    print(sum(100 * get_reflection(pattern) + get_reflection(transpose(pattern)) 
              for pattern in PATTERNS))

def part2():
        print(sum(100 * get_reflection(pattern, 1) + get_reflection(transpose(pattern), 1) 
              for pattern in PATTERNS))

part1()
part2()