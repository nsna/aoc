from utils import day
import re
from collections import defaultdict
from math import prod

LINES = day(3).splitlines()

WIDTH = len(LINES[0]) 
HEIGHT = len(LINES) 

def get_symbol(row, match):
    for y in [row - 1, row, row + 1]:
        for x in range(match.start() - 1, match.end() + 1):
            if (
                0 <= y < HEIGHT
                and 0 <= x < WIDTH
                and LINES[y][x] != "."
                and not LINES[y][x].isdigit()
            ):
                return (y, x)

def part1():
    sum = 0
    for row, line in enumerate(LINES):
        for match in re.finditer(r'(\d+)', line):
            symbol = get_symbol(row, match)
            if symbol:
                symbols[symbol].append(int(match.group(0)))
                sum += int(match.group(0))
    print(sum)

def part2():
    gear_ratios = sum([prod(part_num) for _, part_num in symbols.items() if len(part_num) == 2])
    print(gear_ratios)

symbols = defaultdict(list)
part1()
part2()