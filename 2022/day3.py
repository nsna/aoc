from utils import day
from more_itertools import chunked, divide
from functools import reduce
from string import ascii_letters

RAW = day(3)

values = dict(zip(ascii_letters, range(1,53)))
sacks = RAW.splitlines()

# part1 
print(sum(
    values[reduce(set.intersection, map(set, divide(2, sack))).pop()]
    for sack in sacks
))

# part2
print(sum(
    values[reduce(set.intersection, map(set, group)).pop()]
    for group in chunked(sacks, 3)
))