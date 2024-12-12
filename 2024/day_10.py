from utils import day

GRID = day(10).splitlines()

HEIGHT = len(GRID)
WIDTH = len(GRID[0])

def traverse(nodes):
    y, x = nodes[-1]
    if GRID[y][x] == '9':
        return [nodes]

    paths = []

    for (dy, dx) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        yi, xi = y + dy, x + dx

        if not (0 <= yi < HEIGHT and 0 <= xi < WIDTH):
            continue

        if int(GRID[yi][xi]) - int(GRID[y][x]) == 1 and (yi, xi) not in nodes:
            paths.extend(traverse(nodes + [(yi, xi)]))

    return paths

p1 = 0
p2 = 0

for y in range(HEIGHT):
    for x in range(WIDTH):
        if GRID[y][x] == '0':
            paths = traverse([(y, x)])
            p1 += len(set(path[-1] for path in paths))
            p2 += len(paths)

print(p1)
print(p2)
