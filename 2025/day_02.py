from itertools import batched

from utils import day

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
