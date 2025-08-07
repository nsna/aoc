from collections import deque, defaultdict
from utils import day

RAW = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""
RAW = day(12)
GRID = RAW.splitlines()

HEIGHT = len(GRID)
WIDTH = len(GRID[1])

def adj(y, x):
    # adjacent neighbour with boundary check
    if not (0 <= y < HEIGHT and 0 <= x < WIDTH):
        return '💀'
    else:
        return GRID[y][x]

def rotate(coord):
    y, x = coord
    return (x, -y)

def get_regions():
    coords = set([(y, x) for x in range(WIDTH) for y in range(HEIGHT)])
    regions = []
    while coords:
        origin = coords.pop()
        region = bfs(origin)
        regions.append(region)
        coords -= set(region)
    return {i: region for i, region  in enumerate(regions)}

def bfs(origin):
    visited = [origin]
    stack = deque([origin])
    while stack:
        y, x = stack.popleft()
        for (dy, dx) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            yi, xi = y + dy, x + dx
            neighbour = adj(yi, xi)
            if GRID[y][x] == neighbour and (yi, xi) not in visited:
                visited.append((yi, xi))
                stack.append((yi, xi))

    return visited

REGIONS = get_regions()

def p1():
    # get sum of each 'edge' multiplied by the 'area'
    total = 0
    for region in REGIONS.values():
        perimeter = 0
        for (y, x) in region:
            for (dy, dx) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                yi, xi = y + dy, x + dx
                neighbour = adj(yi, xi)
                if GRID[y][x] != neighbour:
                    perimeter += 1
        total += perimeter * len(region)
    print(total)

def p2():
    """
    counting corners is easier than tracking continuous sides.

    - an exterior corner exists if two perpendicular neighbours are outside its own region
    - an interior corner exists if two perpendicular neighbours are *the same* and a
      diagonal member between them us outside its own region

    the total number of corners = total number of sides
    """
    # map each coordinate to a region
    regions = {
        coord: id
        for id, region in REGIONS.items()
        for coord in region
    }
    def bounded_region(y, x):
        if (y, x) in regions:
            return regions[(y, x)]
        else:
            return -1
    total_fences = defaultdict(int)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            this_region = regions[(y, x)]
            for (dy, dx) in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                row_neighbor = (y + dy, x)
                col_neighbor = (y, x + dx)
                diagonal_neighbor = (y + dy, x + dx)
                # exterior corners
                total_fences[this_region] += (
                    this_region != bounded_region(*row_neighbor)
                    and
                    this_region != bounded_region(*col_neighbor)
                )
                # interior corners
                total_fences[this_region] += (
                    this_region == bounded_region(*row_neighbor)
                    and
                    this_region == bounded_region(*col_neighbor)
                    and
                    this_region != bounded_region(*diagonal_neighbor)
                )
    print(sum(
        len(REGIONS[region]) * total_fences[region]
        for region in REGIONS
    ))

p1()
p2()
