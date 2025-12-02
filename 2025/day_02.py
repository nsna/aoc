from itertools import batched

from utils import day

# RAW = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""
RAW = day(2)

p1 = 0
p2 = 0

for id in RAW.split(","):
    start, end = id.split("-")
    for n in range(int(start), int(end) + 1):
        s = str(n)
        if s[: len(s) // 2] == s[len(s) // 2 :]:
            p1 += n
        for i in range(1, len(s) // 2 + 1):
            if len(set(batched(s, i))) == 1:
                p2 += n
                break

print(p1)
print(p2)
