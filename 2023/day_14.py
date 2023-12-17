from utils import day
from operator import add
import time

start_time = time.time()

GRID = day(14).splitlines()
CUBES = []
HEIGHT = len(GRID)
WIDTH = len(GRID[0])
N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)
TILT_SORTS = {
    N: (lambda x: x,    False),
    E: (lambda x: x[1], True),
    S: (lambda x: x,    True),
    W: (lambda x: x[1], False)
}

for y in range(HEIGHT):
    for x in range(WIDTH):
        if GRID[y][x] == '#':
            CUBES.append((y, x))

def get_rocks():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if GRID[y][x] == 'O':
                yield (y, x)

def tilt(rocks, dir):
    key, reverse = TILT_SORTS[dir]
    to_move = sorted(rocks, key=key, reverse=reverse)
    new_rocks = set()
    for rock in to_move:
        while True:
            next_pos = tuple(map(add, rock, dir))
            y, x = next_pos
            if (next_pos in new_rocks 
                or next_pos in CUBES
                or not (
                    0 <= y < HEIGHT
                    and 0 <= x < WIDTH
                )):
                new_rocks.add(rock)
                break
            else:
                rock = next_pos
    return new_rocks

def rotate(rocks, n=1):
    for _ in range(n):
        for d in [N, W, S, E]:
            rocks = tilt(rocks, d)
    return rocks

def detect_cycle(rocks):
    # initial seed N shift
    rocks = tilt(rocks, N)
    memory = {tuple(rocks): 0}
    for i in range(1, 100_000):
        rocks = rotate(rocks)
        state = tuple(rocks)
        if state in memory:
            return memory[state], i - memory[state], memory
        memory[state] = i
    raise ValueError('no cycle found')

def part1():
    print(sum(HEIGHT - y for (y, _) in tilt(get_rocks(), N)))

def part2():
    start, period, memory = detect_cycle(get_rocks())
    # fast forward to 1_000_000_000
    table = {i: state for state, i in memory.items()}
    remainder = (1_000_000_000 - start) % period
    print(sum(HEIGHT - y for (y, _) in table[start + remainder]))

part1()
part2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))