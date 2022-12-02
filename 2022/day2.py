from utils import day, ints

RAW = day(2)

shapes = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

win = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B'
}

def round(opponent, player):
    score = shapes[player]
    # draw
    if shapes[opponent] == shapes[player]:
        return score + 3
    # win
    if beats[player] == opponent:
        return score + 6
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
draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}
lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}
win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}
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