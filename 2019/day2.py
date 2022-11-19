import utils

RAW = utils.day(2)
DATA = list(utils.ints(RAW))

ops = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y
}

def part_one(noun=12, verb=2):
    p1 = DATA[:]
    p1[1] = noun
    p1[2] = verb
    i = 0
    while i < len(p1):
        if p1[i] == 99:
            break
        op, x, y, pos = p1[i : min(i + 4, len(p1) - 1)]
        p1[pos] = ops[op](p1[x], p1[y])
        i += 4
    return p1[0]
    
def part_two():
    for noun in range(120):
        for verb in range(120):
            if part_one(noun, verb) == 19690720:
                return 100 * noun + verb
    
print(part_one())
print(part_two())