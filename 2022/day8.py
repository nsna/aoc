from utils import day
from itertools import takewhile
from more_itertools import ilen
RAW = day(8)

# RAW = """30373
# 25512
# 65332
# 33549
# 35390"""

grid = RAW.splitlines()

internal = [col[1:-1] for col in grid[1:-1]]

def is_gt(seq):
    s = list(seq)
    return all(s[0] > j for j in s[1:])

def n_vis(seq):
    s = iter(seq)
    a = next(s)
    return ilen(takewhile(lambda x: x < a, s)) + 1
    
def n(seq):
    s = list(seq)
    a = s.pop(0)
    n = 0
    for b in s:
        if a > b:
            n += 1
        else:
            n += 1
            break
    return max(1, n)

# outer edge
visible = (len(grid) * 2) - 2 + (len(grid[0]) * 2) - 2

# iterate over internal range
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        # check up down left right
        up    = [row[x] for row in grid[:y+1]]
        down  = [row[x] for row in grid[y:]]
        left  = grid[y][:x+1]
        right = grid[y][x:]
        
        v = any((
            is_gt(reversed(up)),
            is_gt(down),
            is_gt(reversed(left)),
            is_gt(right)
        ))
        visible += v

print(visible)

# part 2
best_scenery = 0
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        # march up
        up    = [row[x] for row in grid[:y+1]]
        down  = [row[x] for row in grid[y:]]
        left  = grid[y][:x+1]
        right = grid[y][x:]
        
        best_scenery = max(best_scenery,n(reversed(up))* n(down)* n(reversed(left))* n(right))
        
print(best_scenery)
        