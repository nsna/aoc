from utils import day

RAW = day(4)


def remove_rolls(grid):
    height = len(grid)
    width = len(grid[0])

    padded = (
        ["." * (width + 2)] + ["." + row + "." for row in grid] + ["." * (width + 2)]
    )

    new_grid = [list(row) for row in grid]
    changes = 0

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for y in range(height):
        for x in range(width):
            if grid[y][x] != "@":
                continue

            py, px = y + 1, x + 1
            neighbours = sum(padded[py + dy][px + dx] == "@" for dy, dx in directions)

            if neighbours < 4:
                new_grid[y][x] = "x"
                changes += 1

    return changes, ["".join(row) for row in new_grid]


iterations = 0
total_rolls = 0
grid = RAW.splitlines()

while True:
    changes, grid = remove_rolls(grid)
    total_rolls += changes
    iterations += 1
    if changes == 0:
        break
    if iterations == 1:
        print(total_rolls)
print(total_rolls)
