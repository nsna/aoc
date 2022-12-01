import utils

RAW = utils.day(1)
elves = RAW.split('\n\n')
elves = [sum(utils.ints(elf)) for elf in elves]
elves.sort()

print(max(elves))
print(sum(elves[-3:]))