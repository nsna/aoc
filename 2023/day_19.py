from utils import day
import re
from collections import defaultdict

LINES = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""".split('\n\n')
LINES = day(19).split('\n\n')

idx = {'x': 0, 'm': 1, 'a': 2, 's': 3}

def parse():
    bins = defaultdict(list)
    flows, parts = LINES
    for sequence in flows.splitlines():
        flow_name, rules = sequence[:-1].split('{')
        *functions, final = rules.split(',')
        for function in functions:
            (category, op), (number, destination) = function[:2], function[2:].split(':')
            bins[flow_name].append((category, category + op + number, destination))
        bins[flow_name].append(final)

    parts = [[x for x in re.findall(r'\d+', part)] for part in parts.splitlines()]
    return bins, parts

def part1():
    for part in parts:
        address = 'in'
        while True:
            *rules, final = flows[address]
            for (category, fn, dst) in rules:
                if eval(fn.replace(category, part[idx[category]])):
                    break
            else:
                dst = final
            if dst in 'AR':
                flows[dst].append(part)
                break
            else:
                address = dst

    print(sum((int(x) for part in flows['A'] for x in part)))

flows, parts = parse()
part1()