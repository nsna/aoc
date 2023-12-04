import re
from collections import Counter
from utils import day
from math import prod

LINES = day(2).splitlines()

def parse():
    pattern = r'(\d+) (red|green|blue)'
    for game_num, game in enumerate(LINES, start=1):
        most_cubes = Counter()
        for num, colour in re.findall(pattern, game):
            most_cubes[colour] = max(most_cubes[colour], int(num))
        yield game_num, most_cubes

def part1():
    limit = Counter({'red':  12, 'green': 13, 'blue':  14})
    print(sum((game_num for game_num, cubes in games if cubes < limit)))

def part2():
    print(sum(prod(cubes.values()) for _, cubes in games))

games = list(parse())
part1()
part2()