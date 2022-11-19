import utils
import re
import math

def get_directions(data: str) -> list:
    wires = data.split('\n')
    struct = re.compile('((\w)(\d+))')
    wire_values = map(struct.findall, wires)
    return [
        [(value[1], int(value[2])) for value in wire] 
        for wire in wire_values
    ]

def get_coordinates(prev, instruction):
    # could just return a list of all points between
    # the new coordinate and the previous
    direction, distance = instruction
    match direction:
        case 'L':
            return [(prev[0] - x, prev[1]) for x in range(1, distance + 1)]
        case 'R':
            return [(prev[0] + x, prev[1]) for x in range(1, distance + 1)]
        case 'U':
            return [(prev[0], prev[1] + y) for y in range(1, distance + 1)]
        case 'D':
            return [(prev[0], prev[1] - y) for y in range(1, distance + 1)]
    
def manhattan_distance(coord, origin=(0,0)):
    return abs(origin[0] - coord[0]) + abs(origin[1] - coord[1])

RAW = utils.day(3)
DATA = get_directions(RAW)

# don't need actual grid, simulate lines / intersections
# say (0, 0) is the origin [x, y]

wires = []
for wire_instructions in DATA:
    wire = [(0, 0)]
    for instruction in wire_instructions:
        wire.extend(
            get_coordinates(wire[-1], instruction)
        )
    wires.append(wire)

# discard origin points and compare sets
intercepts = set(wires[0][1:]) & set(wires[1][1:])

def part_one():
    closest = min(intercepts, key=manhattan_distance)    
    return manhattan_distance(closest)

def part_two():
    steps = math.inf
    for intercept in intercepts:
        steps = min(steps, wires[0].index(intercept) + wires[1].index(intercept))  
    return steps    
    
print(part_one())
print(part_two())