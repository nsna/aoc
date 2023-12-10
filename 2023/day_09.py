from utils import day
from itertools import pairwise

LINES = day(9).splitlines()

def parse():
    return [[int(n) for n in line.split()] for line in LINES]

def extrapolate(sequence):
    ends = [sequence[-1]]
    while not all(e == 0 for e in sequence):
        sequence = [b - a for a, b in pairwise(sequence)]
        ends.append(sequence[-1])
    return sum(ends)

def part1():
    print(sum(extrapolate(sequence) for sequence in sequences))

def part2():
    print(sum(extrapolate(sequence[::-1]) for sequence in sequences))

sequences = parse()
part1()
part2()