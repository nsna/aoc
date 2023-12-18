from utils import day
from heapq import heappush, heappop

GRID = day(17).splitlines()

H = len(GRID)
W = len(GRID[0])

def parse():
    for y in range(H):
        yield [int(x) for x in GRID[y]]

"""
Because it is difficult to keep the top-heavy crucible going in a straight line for very long, 
it can move at most three blocks in a single direction before it must turn 90 degrees left or right. 

The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
"""

def find_heatloss(minimum_distance=1, maximum_distance=3):
    # Modified Djikstra's algorithm
    # https://www.redblobgames.com/pathfinding/a-star/introduction.html#dijkstra
    # starting at 0, 0 -> seed with neighbours E and S
    # heap structure is (priority, y, x, direction_y, direction_x)
    heap = [(0, 0, 0, 1, 0), (0, 0, 0, 0, 1)]
    heatlosses = {}
    while heap:
        heatloss, y, x, dy, dx = heappop(heap)

        # reached end
        if y == H - 1 and x == W - 1:
            return heatloss
        
        # modification: instead of all neighbours, can only turn left or right 90 degrees
        for dy, dx in ((-dx, dy), (dx, -dy)):
            d_heatloss = 0

            # modification: check up to n spaces in each direction instead of just direct neighbours
            for distance in range(1, maximum_distance + 1):
                yi = y + dy * distance
                xi = x + dx * distance

                # exit march if out of bounds
                if not (0 <= yi < H and 0 <= xi < W):
                    break
                    
                # for each step, add the new heatloss value 
                d_heatloss += GRID[yi][xi]
                new_heatloss = heatloss + d_heatloss

                # look up stored heatloss value for current position, direction 'coming from' unique.
                # if the new heatloss value is smaller, explore that branch by adding to the heap.
                # if the heatloss is not explored yet (not in heatlosses dict), 
                # then always explore it (∞ > any new heatloss value).
                if distance >= minimum_distance:
                    if heatlosses.get((yi, xi, dy, dx), float('inf')) > new_heatloss:
                        heatlosses[yi, xi, dy, dx] = new_heatloss
                        heappush(heap, (new_heatloss, yi, xi, dy, dx))

GRID = list(parse())
def part1():
    print(find_heatloss())

def part2():
    print(find_heatloss(4, 10))

part1()
part2()