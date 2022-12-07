from utils import day
from collections import defaultdict
from copy import deepcopy

RAW = day(7)

commands = RAW.splitlines()

dir = defaultdict(int)
root = []

for cmd in commands:
    match cmd.split():
        case ['$', 'cd', p]:
            if p == '..':
                root.pop()
            else:
                root.append(p)
        case ['$', 'ls']:
            pass
        case ['dir', p]:
            pass
        case [s, f]:
            dir[tuple(root)] += int(s)
            # add file size to each parent
            path = deepcopy(root[:-1])
            while path:
                dir[tuple(path)] += int(s)
                path.pop()

# part1
print(sum([d for d in dir.values() if d <= 100000]))

# part2
free = 70000000 - dir[('/',)]
print(min([d for d in dir.values() if d + free >= 30000000]))
