from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=2)

# regex pattern
line_pattern = r'(?P<command>\w*) (?P<value>[0-9]+)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

horizontal = 0
depth = 0

for pair in input_data:
    if pair.command == 'forward':
        horizontal += int(pair.value)

    if pair.command == 'down':
        depth += int(pair.value)

    if pair.command == 'up':
        depth -= int(pair.value)

# submit answer
puzzle.answer_a = horizontal * depth
