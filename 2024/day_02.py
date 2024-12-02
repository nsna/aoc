import re
from utils import day

RAW = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
RAW = day(2)

VALS = [
    [int(n) for n in re.findall(r'\d+', line)]
    for line in RAW.splitlines()
]

def is_safe(report: list[int]):
    a, b = report[:2]
    delta = (-1) ** (a < b)
    return all(0 < (a - b) * delta < 4 for (a, b) in zip(report, report[1:]))

def p1():
    print(sum(is_safe(report) for report in VALS))

def p2():
    # brute force: check all iterations of dropping a value
    print(sum(
        any(
            is_safe(report[:i] + report[i+1:])
            for i in range(len(report))
        )
        for report in VALS
    ))

p1()
p2()
