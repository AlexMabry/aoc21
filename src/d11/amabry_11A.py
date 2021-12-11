from collections import deque

from aocd import models

from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=11)

# regex pattern
line_pattern = r'(?P<numbers>.*)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

import time
start_time = time.time()
############################
grid = {(ix, iy): int(val) for iy, row in enumerate(input_data) for ix, val in enumerate(row.numbers)}

def axis_range(c):
    return range(max(0, c - 1), min(10, c + 2))

def neighbor_range(p):
    return ((ix, iy) for ix in axis_range(p[0]) for iy in axis_range(p[1]))

total_flashes = 0
for step in range(100):
    grid = {p: val+1 for p, val in grid.items()}
    to_flash = deque(p for p, val in grid.items() if val == 10)

    already_flashed = set()
    while to_flash:
        p = to_flash.pop()
        already_flashed.add(p)

        for np in neighbor_range(p):
            grid[np] += 1

        to_flash.extend((np for np in neighbor_range(p) if grid[np] == 10))

    grid = {p: 0 if p in already_flashed else val for p, val in grid.items()}
    total_flashes += len(already_flashed)
############################
print(time.time() - start_time)

# submit answer
puzzle.answer_a = total_flashes
