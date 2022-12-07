from utils import day
from collections import defaultdict

RAW = day(7)
commands = RAW.splitlines()
dir = defaultdict(int)
cwd = []

for cmd in commands:
    match cmd.split():
        case ['$', 'cd', '..']:
            cwd.pop()
        case ['$', 'cd', p]:
            cwd.append(p)
        case ['$', 'ls']:
            pass
        case ['dir', _]:
            pass
        case [s, f]:
            dir[tuple(cwd)] += int(s)
            # add file size to each parent
            parents = cwd[:-1]
            while parents:
                dir[tuple(parents)] += int(s)
                parents.pop()

# part1
print(sum([d for d in dir.values() if d <= 100_000]))

# part2
free = 70_000_000 - dir[('/',)]
print(min([d for d in dir.values() if d + free >= 30_000_000]))
