from utils import day, ints
import re
from collections import defaultdict, deque
from copy import deepcopy

RAW = day(5)

part1 = defaultdict(deque)
layout, moves = [section.splitlines() for section in RAW.split('\n\n')]
locations = [match.start() for match in re.finditer('\d', layout[-1])]

# sort crates into dict<deque>
for loc in locations:
    for row in layout[-2::-1]:
        crate = row[loc]
        if crate == ' ':
            break
        part1[int(layout[-1][loc])].append(crate)

# need a fresh copy of the input for part 2 since we are modifying it
part2 = deepcopy(part1)

# part 1 & part 2
for move in moves:
    n, a, b = ints(move)
    temp = deque([])
    for _ in range(n):
        part1[b].append(part1[a].pop())
        temp.appendleft(part2[a].pop())
    part2[b].extend(temp)
    
print(''.join([part1[val][-1] for val in part1]))
print(''.join([part2[val][-1] for val in part2]))