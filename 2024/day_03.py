import re
from utils import day

RAW = day(3)

def find_mults(s) -> list[tuple[int, int]]:
    return [(int(a), int(b)) for (a, b) in re.findall(r'mul\((\d+),(\d+)\)', s)]

def p1():
    print(sum(a * b for (a, b) in find_mults(RAW)))

def p2():
    # only care about mul(a,b)|don't|do
    cmds = r"(mul\(\d+,\d+\))|don't(?=\(\))|do(?=\(\))"
    total = 0
    enabled = True
    for match in re.finditer(cmds, RAW):
        cmd = match.group()
        if cmd == "don't":
            enabled = False
        elif cmd == "do":
            enabled = True
        elif enabled:
            total += sum(a * b for (a, b) in find_mults(cmd))

    print(total)

p1()
p2()
