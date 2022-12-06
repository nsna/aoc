from utils import day
from more_itertools import sliding_window

RAW = day(6)

# part1
for i, window in enumerate(sliding_window(RAW, 4)):
    if len(set(window)) == 4:
        print(i + 4)
        break
        
# part2
for i, window in enumerate(sliding_window(RAW, 14)):
    if len(set(window)) == 14:
        print(i + 14)
        break
