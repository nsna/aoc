import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from utils import day

RAW = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
# RAW = day(10)


def parse(raw_data):
    for line in raw_data.splitlines():
        lights, *buttons, joltage = line.split()
        lights = np.array([1 if c == "#" else 0 for c in lights[1:-1]], dtype=int)
        num_rows = len(lights)
        num_cols = len(buttons)
        A = np.zeros((num_rows, num_cols), dtype=int)
        for col_idx, button in enumerate(buttons):
            affected_rows = [int(x) for x in button[1:-1].split(",")]
            A[affected_rows, col_idx] = 1
        joltage = np.array(joltage[1:-1].split(","), dtype=int)

        yield A, lights.reshape(-1, 1), joltage.reshape(-1, 1)


def solve_min_moves_gf2(A, b):
    rows, cols = A.shape
    M = np.hstack([A, b])

    # Gauss-Jordan Elimination
    pivots = []
    pivot_row = 0

    for col in range(cols):
        if pivot_row >= rows:
            break

        # Find pivot (first 1 in column from pivot_row down)
        candidates = np.where(M[pivot_row:, col] == 1)[0]
        if candidates.size == 0:
            continue

        # Swap pivot row to current position
        curr = candidates[0] + pivot_row
        M[[pivot_row, curr]] = M[[curr, pivot_row]]

        # Eliminate 1s in this column for all other rows (Vectorized XOR)
        mask = M[:, col] == 1
        mask[pivot_row] = False
        M[mask] ^= M[pivot_row]

        pivots.append((pivot_row, col))
        pivot_row += 1

    # If any row is [0...0 | 1], it's unsolvable
    for r in range(pivot_row, rows):
        if M[r, -1] == 1:
            return None

    # Extract particular solution
    x_particular = np.zeros(cols, dtype=int)
    pivot_rows, pivot_cols = map(list, zip(*pivots))
    x_particular[pivot_cols] = M[pivot_rows, -1]

    # Explore null space free variables to find smallest solution
    free_cols = [c for c in range(cols) if c not in pivot_cols]

    if not free_cols:
        return x_particular

    num_free = len(free_cols)

    # Build null basis matrix
    null_basis = np.zeros((num_free, cols), dtype=int)

    # Set the free variable 'diagonal'
    null_basis[np.arange(num_free), free_cols] = 1

    # Set the pivot variables (Back-substitution via Slicing)
    # Map the influence of free vars onto pivot rows
    null_basis[:, pivot_cols] = M[pivot_rows][:, free_cols].T

    # Generate all possible coefficients (Truth Table for k free vars)
    # Uses bitwise math to generate table: [[0,0], [0,1], [1,0], [1,1]]...
    # Shape: (2^k, k)
    coeffs = (np.arange(1 << num_free)[:, None] >> np.arange(num_free)) & 1

    # Calculate all offsets at once: Coeffs @ Basis
    # Shape: (2^k, cols)
    offsets = (coeffs @ null_basis) % 2

    # Add offsets to particular solution
    candidates = (x_particular + offsets) % 2

    # Find the candidate with minimum moves (Sum of 1s)
    move_counts = candidates.sum(axis=1)
    best_idx = np.argmin(move_counts)

    return candidates[best_idx]


def solve_linear(A, b):
    c = np.ones(A.shape[1])
    b_flat = b.flatten()
    constraints = LinearConstraint(A, lb=b_flat, ub=b_flat)
    bounds = Bounds(lb=0, ub=np.inf)
    res = milp(c=c, constraints=constraints, bounds=bounds, integrality=1)
    return np.sum(res.x)


machines = list(parse(RAW))
print(sum([np.sum(solve_min_moves_gf2(A, b)) for (A, b, _) in machines]))
print(sum([solve_linear(A, b) for (A, _, b) in machines]))
