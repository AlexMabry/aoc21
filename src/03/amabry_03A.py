from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=3)

# regex pattern
line_pattern = r'([01])([01])([01])([01])([01])([01])([01])([01])([01])([01])([01])([01])'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
totals = [0] * 12
for bits in input_data:
    for pos in range(12):
        totals[pos] += (1 if bits[pos] == "1" else -1)

gamma = sum([2 ** (11-pos) for pos in range(12) if totals[pos] > 0])
epsilon = sum([2 ** (11-pos) for pos in range(12) if totals[pos] <= 0])
############################

# submit answer
puzzle.answer_a = gamma * epsilon
