from utils import day, pos_ints

RAW = day(4)

pairs = RAW.splitlines()
subsets = 0
overlaps = 0

for pair in pairs:
    a1,a2,b1,b2 = pos_ints(pair)
    a = set(range(a1, a2 + 1))
    b = set(range(b1, b2 + 1))
    # part1
    subsets += (a.issubset(b) or b.issubset(a))
    # part2
    overlaps += len(a & b) > 0
    
print(subsets)
print(overlaps)