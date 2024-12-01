from utils import day
from copy import deepcopy

RAW = day(1)

lines = RAW.splitlines()
BIN_A = []
BIN_B = []

for line in lines:
    a, b = line.split('   ')
    BIN_A.append(int(a))
    BIN_B.append(int(b))

def p1():
    bin_a = deepcopy(BIN_A)
    bin_b = deepcopy(BIN_B)

    sums = 0
    els = len(bin_a)
    for _ in range(els):
        min_a = min(bin_a)
        bin_a.remove(min_a)
        min_b = min(bin_b)
        bin_b.remove(min_b)
        sums += abs(min_a - min_b)

    print(sums)

def p2():
    score = 0
    for el in BIN_A:
        score += el * BIN_B.count(el)
    
    print(score)

p1()
p2()