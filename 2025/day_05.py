from bisect import bisect_right

from utils import day

RAW = day(5)

fresh_ranges, ingredients = RAW.split("\n\n")
intervals = sorted(
    [
        [int(a), int(b)]
        for line in fresh_ranges.splitlines()
        for (a, b) in [line.split("-")]
    ]
)
merged = []
for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])


def is_fresh(intervals, n):
    pos = bisect_right(intervals, n, key=lambda x: x[0])
    if pos == 0:
        return False
    interval_candidate = intervals[pos - 1]
    return n <= interval_candidate[1]


print(sum([is_fresh(merged, int(val)) for val in ingredients.splitlines()]))
print(sum([end - start + 1 for start, end in merged]))
