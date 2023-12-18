from utils import day
import time

start_time = time.time()
PLAN = day(18).splitlines()

def parse():
    d1 = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    d2 = {'3': (-1, 0), '1': (1, 0), '0': (0, 1), '2': (0, -1)}
    p1_steps, p2_steps = [], []
    for line in PLAN:
        dir, dist, colour = line.split()
        p1_steps.append((d1[dir], int(dist)))
        p2_steps.append((d2[colour[7:8]], int(colour[2:7], 16)))
    return p1_steps, p2_steps

def area(steps):
    y = x = 0
    perimeter = 0
    vertices = []
    for (dy, dx), distance in steps:
        perimeter += distance
        y += dy * distance
        x += dx * distance
        vertices.append((y, x))
    # shoelace theorem
    a = 0
    b = 0
    n = len(vertices)
    for i in range(n):
        a += vertices[i][1] * vertices[(i + 1) % n][0]
        b += vertices[i][0] * vertices[(i + 1) % n][1]
    total_area = abs(a - b) / 2
    intersecting_with_edges = (perimeter / 2) - 1
    print(total_area - intersecting_with_edges + perimeter)

def part1():
    area(p1_steps)

def part2():
    area(p2_steps)

p1_steps, p2_steps = parse()
part1()
part2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))