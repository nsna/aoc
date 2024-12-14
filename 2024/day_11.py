from utils import day
from functools import cache

RAW = "125 17"
RAW = day(11)

def stones():
    return map(int, RAW.split())

@cache
def blink(stone, depth) -> int:
    str_stone = str(stone)
    if depth == 0:
        return 1
    if stone == 0:
        return blink(1, depth - 1)
    elif (l:=len(str_stone)) % 2 == 0:
        left, right = int(str_stone[:l//2]), int(str_stone[l//2:])
        return blink(left, depth - 1) + blink(right, depth - 1)
    else:
        return blink(stone * 2024, depth - 1)

def p1():
    print(sum(blink(stone, 25) for stone in stones()))

def p2():
    print(sum(blink(stone, 75) for stone in stones()))

p1()
p2()
