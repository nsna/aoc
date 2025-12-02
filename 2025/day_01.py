from utils import day

RAW = day(1)

dial = 50
p1 = 0
p2 = 0

for move in RAW.splitlines():
    direction = move[0]
    distance = int(move[1:])
    for _ in range(distance):
        if direction == "L":
            dial -= 1
        else:
            dial += 1
        if dial == 0 or dial == 100:
            p2 += 1
        dial %= 100
    if dial == 0:
        p1 += 1

print(p1)
print(p2)
