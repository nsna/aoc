from utils import day
from math import prod

RAW = day(8)
grid = RAW.splitlines()

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
    up    = [row[x] for row in grid[:y+1]][::-1] # reverse
    down  = [row[x] for row in grid[y:]]
    left  = grid[y][:x+1][::-1] # reverse
    right = grid[y][x:]
    return (up, down, left, right)

# start part1 with the grid edge length
part1 = (len(grid) - 1) * 4
part2 = 0

# iterate over internal range
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        part1 += any(map(clear_view, los(x, y)))
        part2  = max(part2, prod(map(trees_seen, los(x, y))))
         
print(part1)
print(part2)
