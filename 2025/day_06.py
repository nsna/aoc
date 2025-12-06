from itertools import accumulate
from operator import add, mul

with open("inputs/day_06.txt") as fh:
    RAW = fh.read()

OPS = {"*": mul, "+": add}


def calc(lines):
    result = 0
    for row in lines:
        op, *vals = row
        acc = accumulate(map(int, vals), OPS[op])
        *_, val = acc
        result += val
    return result


def scan(lines):
    numbers = []
    width = max(len(line) for line in lines)
    height = len(lines)
    group = []
    op = " "
    for x in range(width):
        col = [f"{line:<{width}}"[x] for line in lines[:-1]]
        if f"{lines[-1]:<{width}}"[x] != " ":
            op = lines[-1][x]
        if col == [" "] * (height - 1):
            numbers.append(group + [op])
            group = []
            op = " "
        else:
            group.append(int("".join(col)))
    numbers.append(group + [op])
    return numbers


print(p1 := calc(zip(*[line.split() for line in RAW.splitlines()][::-1])))
print(p2 := calc(map(reversed, scan(RAW.splitlines()))))
