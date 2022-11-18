import utils
import math

RAW = utils.day(1)
DATA = list(utils.extract_ints(RAW))

def calc_fuel(mass: int):
    return max(math.floor(mass / 3) - 2, 0)

def collapse(mass: int, total: int = 0):
    remaining = calc_fuel(mass)
    if remaining == 0:
        return total
    else:
        return collapse(remaining, total+remaining)

def part_one():
    return sum(map(calc_fuel, DATA))

def part_two():
    return sum(map(collapse, DATA))

if __name__ == "__main__":
    print("part 1:", part_one())
    print("part 2:", part_two())