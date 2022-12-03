from utils import day
from more_itertools import chunked
from functools import reduce
from string import ascii_letters

RAW = day(3)

values = dict(zip(ascii_letters, range(1,53)))
sacks = RAW.splitlines()

# part1 
total = 0
for sack in sacks:
    l = len(sack)
    shared = set(sack[:l//2]) & set(sack[l//2:])
    total += values[shared.pop()]

print(total)

# part2
total = 0
for group in chunked(sacks, 3):
    badge = reduce(set.intersection, map(set, group))
    total += values[badge.pop()]

print(total)