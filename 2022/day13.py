from utils import day
from itertools import chain, accumulate
from functools import cmp_to_key
from operator import mul

RAW = day(13)

packets = [
    [eval(packet) for packet in pair.split('\n')]
    for pair in RAW.split('\n\n')
]

def cmp(a, b):
    # returning a negative result indicates a pair is in correct order
    match a, b:
        case int(), int():
            return a - b
        case int(), _:
            a = [a]
        case _, int():
            b = [b]
    
    # result should be 2 lists now

    # map
    # Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
    it = filter(None, map(cmp, a, b))

    # next(iterator, default)
    # If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.
    return next(it, len(a) - len(b))

def part1():
    return sum(i for i, (a, b) in enumerate(packets, start=1) if cmp(a, b) < 0)

def part2():
    flat_packets = chain.from_iterable(packets)
    flat_packets = chain([[[2]], [[6]]], flat_packets)
    sorted_packets = sorted(flat_packets, key=cmp_to_key(cmp))
    return max(accumulate(
        (i for i, packet in enumerate(sorted_packets, start=1) 
        if packet == [[2]] or packet == [[6]]),
        func=mul
    ))

print(part1())
print(part2())