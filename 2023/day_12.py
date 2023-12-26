from utils import day
from functools import cache

LINES = day(12).splitlines()

def parse():
    for nonogram in LINES:
        line, groups = nonogram.split()
        yield line, tuple(map(int, groups.split(',')))

# derived from
# https://github.com/fuglede/adventofcode/blob/master/2023/day12/solutions.py
# since it made the most sense

@cache
def solutions(line, groups, group_idx=0):
    if not line:
        # the group index only reliably gets closed out if there is a trailing '.'
        # to simplify the check, this is why a '.' is appended to all lines
        return not groups and not group_idx
    n = 0
    # If next letter is a "?", we branch, otherwise just consider next character
    options = [".", "#"] if line[0] == "?" else line[0]
    for c in options:
        if c == "#":
            # Extend current group
            n += solutions(line[1:], groups, group_idx + 1)
        else:
            if group_idx:
                # If we were in a group that can be closed, close it
                if groups and groups[0] == group_idx:
                    n += solutions(line[1:], groups[1:])
            else:
                # If we are not in a group, move on to next symbol
                n += solutions(line[1:], groups)
    return n

nonograms = list(parse())

def part1():
    print(sum(solutions(line + '.', groups) for line, groups in nonograms))

def part2():
    print(sum(solutions('?'.join([line] * 5) + '.', groups * 5) for line, groups in nonograms))

part1()
part2()