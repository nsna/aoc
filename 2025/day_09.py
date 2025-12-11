from collections import deque
from dataclasses import dataclass
from itertools import combinations

from utils import day

RAW = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
RAW = day(9)


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def manhattan_dist(self, other: "Point") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def rect_area(self, other: "Point") -> int:
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)


def parse_points(raw_data: str) -> list[Point]:
    return [
        Point(int(x), int(y))
        for line in raw_data.splitlines()
        if line.strip()
        for x, y in [line.split(",")]
    ]


def get_segment_len(grid_idx: int, coords: list[int]) -> int:
    """Returns the real-world length of a grid segment (wall or gap)."""
    # Case 1: Odd Index = A Wall (grid mapped as 2*x + 1)
    if grid_idx % 2 != 0:
        return 1

    # Case 2: Even Index = Gap
    if grid_idx == 0:
        return 0

    # Calculate index in the original sorted coordinate list
    # Grid 2 (Space) -> lies between Wall 1 (coords[0]) and Wall 3 (coords[1])
    idx = (grid_idx // 2) - 1

    if idx < 0 or idx >= len(coords) - 1:
        return 0

    return max(0, coords[idx + 1] - coords[idx] - 1)


def solve(raw_input: str):
    points = parse_points(raw_input)

    # Part 1
    _, p1, p2 = max((a.manhattan_dist(b), a, b) for a, b in combinations(points, 2))
    print(f"Part 1: {p1.rect_area(p2)}")

    # Part 2
    # Coordinate compression
    xs = sorted(list({p.x for p in points}))
    ys = sorted(list({p.y for p in points}))
    x_map = {val: i for i, val in enumerate(xs)}
    y_map = {val: i for i, val in enumerate(ys)}

    # Virtual grid
    W = 2 * len(xs) + 1
    H = 2 * len(ys) + 1
    grid = [["." for _ in range(W)] for _ in range(H)]

    # Fill walls
    num_points = len(points)
    edges = [(points[i], points[(i + 1) % num_points]) for i in range(num_points)]

    for start, end in edges:
        xi1, yi1 = 2 * x_map[start.x] + 1, 2 * y_map[start.y] + 1
        xi2, yi2 = 2 * x_map[end.x] + 1, 2 * y_map[end.y] + 1

        # Fill range inclusive
        r_x = range(min(xi1, xi2), max(xi1, xi2) + 1)
        r_y = range(min(yi1, yi2), max(yi1, yi2) + 1)

        for y in r_y:
            for x in r_x:
                grid[y][x] = "#"

    # Flood fill outside
    # Start from (0,0) which is guaranteed to be padding/outside
    queue = deque([(0, 0)])
    visited = {(0, 0)}
    grid[0][0] = "O"

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < W and 0 <= ny < H:
                if (nx, ny) not in visited and grid[ny][nx] != "#":
                    visited.add((nx, ny))
                    grid[ny][nx] = "O"
                    queue.append((nx, ny))

    # Prefix Sum for Valid Areas
    # Valid areas are those NOT marked 'O' (so '.' interior and '#' walls)
    prefix_sum = [[0] * W for _ in range(H)]

    for y in range(H):
        for x in range(W):
            cell_area = 0
            if grid[y][x] != "O":
                cell_area = get_segment_len(x, xs) * get_segment_len(y, ys)

            top = prefix_sum[y - 1][x] if y > 0 else 0
            left = prefix_sum[y][x - 1] if x > 0 else 0
            top_left = prefix_sum[y - 1][x - 1] if y > 0 and x > 0 else 0

            prefix_sum[y][x] = cell_area + top + left - top_left

    # helper to calculate area
    def get_area_sum(x1, y1, x2, y2):
        total = prefix_sum[y2][x2]
        left_chunk = prefix_sum[y2][x1 - 1] if x1 > 0 else 0
        top_chunk = prefix_sum[y1 - 1][x2] if y1 > 0 else 0
        corner_chunk = prefix_sum[y1 - 1][x1 - 1] if x1 > 0 and y1 > 0 else 0
        return total - left_chunk - top_chunk + corner_chunk

    # Find Max Rectangle
    max_area = 0

    for p1, p2 in combinations(points, 2):
        # Map to grid coordinates
        x1, x2 = sorted((2 * x_map[p1.x] + 1, 2 * x_map[p2.x] + 1))
        y1, y2 = sorted((2 * y_map[p1.y] + 1, 2 * y_map[p2.y] + 1))

        # Compare areas
        expected = p1.rect_area(p2)
        actual = get_area_sum(x1, y1, x2, y2)

        if actual == expected:
            max_area = max(max_area, actual)

    print(f"Part 2: {max_area}")


if __name__ == "__main__":
    solve(RAW)
