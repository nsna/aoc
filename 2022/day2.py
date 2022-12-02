from utils import day, rshift

RAW = day(2)

a = ['A', 'B', 'C']
b = ['X', 'Y', 'Z']

shapes = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

win = dict(zip(b, rshift(a, 1)))

def round(a, b):
    score = shapes[b]
    # draw
    if shapes[a] == shapes[b]:
        return score + 3
    # win
    if win[b] == a:
        return score + 6
    # lose
    else:
        return score

moves = [move.split() for move in RAW.split('\n')]
score = 0
for move in moves:
    score += round(*move)

print(score)

# part 2
# X = lose
# Y = draw
# Z = win
draw = dict(zip(a, rshift(b, 0)))
lose = dict(zip(a, rshift(b, 1)))
win  = dict(zip(a, rshift(a, 2)))

score = 0
for move in moves:
    opponent, outcome = move
    if outcome == 'X':
        score += shapes[lose[opponent]]
    if outcome == 'Y':
        score += shapes[draw[opponent]] + 3
    if outcome == 'Z':
        score += shapes[win[opponent]] + 6

print(score)       