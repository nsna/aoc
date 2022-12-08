from utils import day, int_grid
from math import prod

RAW = day(8)
rows = int_grid(RAW)
cols = list(zip(*rows))

def clear_view(seq) -> bool:
    """
    Returns True if the first tree is higher than the rest of the trees
    in the sequence
    """
    s = iter(seq)
    a = next(s)
    return all(a > b for b in s)

def trees_seen(seq) -> int:
    """
    Returns number of trees shorter than first tree
    If a tree is higher/equal, return early (but still counts as seen)
    """
    s = iter(seq)
    a = next(s)
    n = 0
    for b in s:
        if a > b:
            n += 1
        else:
            return n + 1
    return n
    
def los(x, y) -> tuple:
    """
    Return lines of sight to grid edges from (x, y) in 4 directions
    Some sequences are reversed so the order is always origin -> edge
    """
    up    = cols[x][y::-1]
    down  = cols[x][y:]     
    left  = rows[y][x::-1]
    right = rows[y][x:]
    return (up, down, left, right)

# start part1 with the grid edge length
part1 = (len(rows) - 1) * 4
part2 = 0

# iterate over internal range
for y in range(1, len(rows) - 1):
    for x in range(1, len(cols) - 1):
        part1 += any(map(clear_view, los(x, y)))
        part2  = max(part2, prod(map(trees_seen, los(x, y))))
         
print(part1)
print(part2)