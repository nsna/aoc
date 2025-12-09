import heapq
import math
from itertools import combinations

from utils import day

RAW = day(8)


class Point:
    def __init__(self, x_coord, y_coord, z_coord):
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        dz = self.z - other_point.z

        distance_sq = (dx**2) + (dy**2) + (dz**2)

        return math.sqrt(distance_sq)


class DisjointSetUnion:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.size = {node: 1 for node in nodes}
        self.active_roots = set(nodes)

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                survivor = root_j
                absorbed = root_i
            else:
                survivor = root_i
                absorbed = root_j

            self.parent[absorbed] = survivor
            self.size[survivor] += self.size[absorbed]

            self.active_roots.remove(absorbed)
            return True
        return False

    def get_current_sizes(self):
        return [self.size[root] for root in self.active_roots]


points = [
    Point(int(x), int(y), int(z))
    for line in RAW.splitlines()
    for x, y, z in [line.split(",")]
]
adjacency_list = sorted([(a.distance_to(b), a, b) for a, b in combinations(points, 2)])
dsu = DisjointSetUnion(points)

p1_limit = 999
i = 0
while True:
    weight, point_a, point_b = adjacency_list[i]
    dsu.union(point_a, point_b)
    if i == p1_limit:
        print(p1 := math.prod(heapq.nlargest(3, dsu.get_current_sizes())))
    if len(dsu.get_current_sizes()) == 1:
        print(p2 := point_a.x * point_b.x)
        break
    i += 1
