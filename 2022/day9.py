from utils import day
import numpy as np

RAW = day(9)

class Knot:
    def __init__(self, tail=None):
        self.tail = tail
        self.pos = np.array([0, 0])
        self.visited = {(0,0)}
        
    def move(self, delta):
        self.pos += delta
        if self.tail:
            d = self.pos - self.tail.pos
            # inf matrix norm = max(sum(abs(x), axis=1))
            if np.linalg.norm(d, np.inf) > 1:
                self.tail.move(np.clip(d, -1, 1))
        else:
            self.visited.add(tuple(self.pos))

def parse():
    deltas = dict(U = (0,  1), D = (0, -1), L = (-1,  0), R = (1,  0))
    for cmd in RAW.splitlines():
        dir, dis = cmd.split()
        yield deltas[dir], int(dis)

def march(knots: list) -> int:
    commands = RAW.splitlines()
    H = knots[-1]
    T = knots[ 0]
    for dir, dis in parse():
        for _ in range(dis):
            H.move(dir)
    return len(T.visited)

def make_rope(n: int):
    knots = []
    for i in range(n):
        tail = knots[-1] if knots else None
        knots.append(Knot(tail))
    return knots

print(march(make_rope(2)))
print(march(make_rope(10)))