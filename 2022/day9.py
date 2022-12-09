from utils import day, pretty_grid
import numpy as np
from functools import partial
from rich import print

RAW = day(9)

# RAW = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

deltas = dict(
    U = np.array(( 0,  1)),
    D = np.array(( 0, -1)),
    L = np.array((-1,  0)),
    R = np.array(( 1,  0))
)

H = np.array([0, 0])
T = np.array([0, 0])

commands = RAW.splitlines()
visited = set([(0,0)])

for cmd in commands:
    dir, dis = cmd.split()
    dis = int(dis)
    for _ in range(dis):
        # move head
        H += deltas[dir]
        # move tail
        # check distance, not touching if x or y > 1
        d = (H - T)
        if np.any((d > 1)|(d < -1)):
            T += np.clip(d, -1, 1)
            visited.add(tuple(T))
        # pretty_grid([H,T])

print(len(visited))
# pretty_grid(visited)
