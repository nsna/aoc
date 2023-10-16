from utils import ints, manhattan_distance, day

RAW = day(15)

NOT_FOUND = 0

class BeaconDict(dict):
    def __missing__(self, key):
        return NOT_FOUND
    
def parse():
    sensors = {}
    beacons = BeaconDict()
    for sensor in RAW.splitlines():
        x1, y1, x2, y2 = ints(sensor)
        # map sensor: distance_to_beacon
        sensors[x1, y1] = manhattan_distance((x1, y1), (x2, y2))
        beacons[x2, y2] = 1
    return sensors, beacons

def part1(line):
    left = right = 0
    for x, y in sensors:
        dist_from_line = abs(line - y)
        intersect = sensors[(x, y)] - dist_from_line
        if intersect >= 0:
            left = min(left, x - intersect)
            right = max(right, x + intersect + 1)

    # remove any beacons on the line
    right -= sum(beacon for (_, y), beacon in beacons.items() if y == line)
    print(right-left)

def part2(depth):
    for line in range(depth + 1):
        scans = []
        for x, y in sensors:
            dist_from_line = abs(line - y)
            intersect = sensors[(x, y)] - dist_from_line
            if intersect >= 0:
                scans.append((x - intersect, x + intersect))
        # sort the ranges so it's easier to merge
        scans.sort()
        _, right = scans.pop(0)
        # attempt to merge the scan ranges, break if not continuous
        for start, end in scans:
            continuous = True
            if start - right > 1:
                continuous = False
                print((right + 1) * 4000000 + line)
                break
            else:
                right = max(right, end)
        if not continuous:
            break

sensors, beacons = parse()
part1(2000000)
part2(4000000)