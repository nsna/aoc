from utils import ints

RAW = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

SENSOR = 1
BEACON = 2

def parse():
    cave = {}
    for sensor in RAW.splitlines():
        x1, y1, x2, y2 = ints(sensor)
        cave[x1, y1] = SENSOR
        cave[x2, y2] = BEACON
    return cave

def print_cave():
    min_x = min(key[0] for key in cave.keys())
    max_x = max(key[0] for key in cave.keys())
    min_y = min(key[1] for key in cave.keys())
    max_y = max(key[1] for key in cave.keys())

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = [['.' for _ in range(width)] for _ in range(height)]
    for (x, y), value in cave.items():
        if value == SENSOR:
            grid[y - min_y][x - min_x] = 'S'
        elif value == BEACON:
            grid[y - min_y][x - min_x] = 'B'
    
    for row in grid:
        print(''.join(row))


def part1(line = 10):
    # 1. on the given line find closest sensor
    # 2. find number of positions N on the line the sensor field encorporates
    # 3. find next closest sensor to the line
    # 4. repeat until no changes to N occur
    candidates = sorted(
        [key for key in cave.keys() if cave[key] == SENSOR], 
        key = lambda xy: abs(line - xy[1]))
    print(candidates)


cave = parse()
part1()
#print_cave()
#print(cave)