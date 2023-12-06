import re
from math import prod, sqrt
import time
from utils import day

start_time = time.time()
LINES = day(6)

ints = re.findall(r'\d+', LINES)
races = zip(map(int, ints[:4]), map(int, ints[4:]))
p2_time = int(''.join(ints[:4]))
p2_dist = int(''.join(ints[4:]))

def roots(b, c):
    """
    d = x * (t - x)
    d = xt - x^2
    x^2 - xt + d = 0
    ∴ a = 1, b = time, c = distance
    """
    root_a = (-b + sqrt(b**2 - 4*c)) / 2
    root_b = (-b - sqrt(b**2 - 4*c)) / 2
    return abs(int(root_a) - int(root_b))

def part1():
    print(prod([roots(p1_time, p1_dist) for p1_time, p1_dist in races]))

def part2():
    print(roots(p2_time, p2_dist))

part1()
part2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))