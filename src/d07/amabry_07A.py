from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=7)

# regex pattern
line_pattern = r'(?P<group_name>.*)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=False, is_numbers=False, regex=None)
crabs = sorted(int(n) for n in input_data.split(','))

import time
start_time = time.time()
############################
dist = {n: crab_count for n in range(max(crabs)+1) if (crab_count := crabs.count(n)) > 0}

min_fuel = 1_000_000
for this_num in range(max(crabs)+1):
    this_fuel = 0
    for n, crab_count in dist.items():
        this_fuel += abs(this_num - n) * crab_count

    min_fuel = min(this_fuel, min_fuel)
############################
print(time.time() - start_time)

# submit answer
puzzle.answer_a = min_fuel
