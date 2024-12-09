import re
from itertools import product, chain, zip_longest

from utils import day

RAW = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
#RAW = day(7)

EQNS = [[int(n) for n in re.findall(r'\d+', line)] for line in RAW.splitlines()]
OPS = ['+', '*']
OPS_2 = ['+', '*', '||']

def parenthesise(vars: list) -> str:
    pair, remaining = vars[:3], vars[3:]
    if pair[1] == '||':
        pair = [str(eval(pair[0])) + pair[2]]
    if remaining == []:
        return ''.join(pair)
    return parenthesise([''.join(['('] + pair + [')'])] + remaining)

def intersperse(vars: list, ops: list):
    for seq in product(ops, repeat=len(vars) - 1):
        yield list(
            str(el) for el in chain.from_iterable(
                zip_longest(vars, seq)
            )
            if el is not None
        )

def is_valid(target, vars, operators):
    return any(target == eval(parenthesise(option)) for option in intersperse(vars, operators))

def p1():
    s = 0
    for eqn in EQNS:
        target, *vars = eqn
        valid = any(target == eval(parenthesise(option)) for option in intersperse(vars, OPS))
        if valid:
            s += target
    print(s)

def p2():
    s = 0
    for eqn in EQNS:
        target, *vars = eqn
        valid = any(target == eval(parenthesise(option)) for option in intersperse(vars, OPS_2))
        if valid:
            s += target
    print(s)

p1()
p2()
