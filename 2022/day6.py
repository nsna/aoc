from utils import day
from more_itertools import sliding_window, all_unique

RAW = day(6)

# part1
for i, window in enumerate(sliding_window(RAW, 4)):
    if all_unique(window):
        print(i + 4)
        break
        
# part2
for i, window in enumerate(sliding_window(RAW, 14)):
    if all_unique(window):
        print(i + 14)
        break
