from utils import day
import time

start_time = time.time()

layout = day(16).splitlines()
N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
height = len(layout)
width = len(layout[0])

def march(start):
    branches = set()
    visited = set()
    stack = [start]
    while stack:
        y, x, dy, dx = stack.pop()
        # prevent infinite loops, only explore new branches
        if (y, x, dy, dx) in branches:
            continue
        branches.add((y, x, dy, dx))

        y += dy
        x += dx

        if not (0 <= y < height and 0 <= x < width):
            continue

        match layout[y][x]:
            case "/":
                dy, dx = -dx, -dy
            case "\\":
                dy, dx = dx, dy
            case "|" if dx:
                stack.append((y, x, *N))
                dy, dx = S
            case "-" if dy:
                stack.append((y, x, *W))
                dy, dx = E

        visited.add((y, x))
        stack.append((y, x, dy, dx))

    return len(visited)

def part1():
    # beams start from outside the grid
    print(march((0, -1, *E)))

def part2():
    s = [(-1, x, *S) for x in range(width)]
    n = [(height, x, *N) for x in range(width)]
    e = [(y, -1, *E) for y in range(height)]
    w = [(y, width, *W) for y in range(height)]
    print(max(march(start) for start in n+s+e+w))

part1()
part2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))