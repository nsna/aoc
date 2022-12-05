from utils import day, ints
import re
from collections import defaultdict, deque
from copy import deepcopy

RAW = day(5)

bins = defaultdict(deque)
layout, moves = [section.splitlines() for section in RAW.split('\n\n')]
locations = [match.start() for match in re.finditer('\d', layout[-1])]

# my input function broke, yaml clipped the leading whitespace...
# need to fix this later
layout[0] = "    " + layout[0]

# sort crates into bins
for loc in locations:
    for row in layout[-2::-1]:
        crate = row[loc]
        if crate == ' ':
            break
        bins[int(layout[-1][loc])].append(crate)

# need a fresh copy of the input for part 2 since we are modifying it
part2 = deepcopy(bins)

# part 1
for move in moves:
    n, a, b = ints(move)
    for _ in range(n):
        bins[b].append(bins[a].pop())

# part 2
for move in moves:
    n, a, b = ints(move)
    temp = deque([])
    for _ in range(n):
        temp.append(part2[a].pop())
    temp.reverse()
    part2[b].extend(temp)
        
print(''.join([bins[val][-1] for val in bins]))
print(''.join([part2[val][-1] for val in part2]))