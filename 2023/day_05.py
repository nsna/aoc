from utils import day
import re
from itertools import batched
import math

LINES = day(5)

def parse():
    sections = LINES.split('\n\n')
    seeds = [int(x) for x in sections[0].split(':')[1].split()]
    maps = []
    for section in sections[1:]:
        _map = {}
        for dst, src, length in batched(map(int, re.findall(r'(\d+)', section)), 3):
            _map[src, src + length] = (dst, dst + length)
        maps.append(_map)
    return list(seeds), maps

def seed_path(seed, m):
    val = seed
    for _map in m:
        val = next(iter([dst[0] + (val - src[0]) for src, dst in _map.items() if src[0] <= val <= src[1]]), None) or val
    return val

def part1():
    min_value = math.inf
    for seed in seeds:
        min_value = min(min_value, seed_path(seed, maps))
    print(min_value)

def part2():
    seed_ranges = [(start, start + end) for start, end in batched(seeds, 2)]
    inverse_maps = [{v: k for k, v in _map.items()} for _map in maps[::-1]]
    loc = 0
    while loc < 199_602_917:
        val = seed_path(loc, inverse_maps)
        seed_exists = next(iter([val for start, end in seed_ranges if start <= val <= end]), None)
        if seed_exists:
            print(loc)
            break
        else:
            loc += 1

seeds, maps = parse()
part1()
part2()