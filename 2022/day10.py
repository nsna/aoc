from utils import day
from functools import partial
from operator import add

RAW = day(10)

def parse():
    for cmd in RAW.splitlines():
        match cmd.split():
            case ['noop']:
                yield partial(add, 0)
            case ['addx', n]:
                yield from (
                    partial(add, 0),
                    partial(add, int(n))
                )

X = 1
checks = [20, 60, 100, 140, 180, 220]
part1 = cycle = offset = 0
out = ""

for op in parse():
    cycle += 1
    out += "#" if offset in (X-1, X, X+1) else "."
    if cycle in checks:
        part1 += X * cycle
    X = op(X)
    offset += 1
    if offset % 40 == 0:
        print(out)
        out = ""
        offset = 0

print(part1)