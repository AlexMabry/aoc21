from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=13)
line_pattern = r'(?:fold along (?P<axis>[xy])=(?P<val>[0-9]+))|(?:(?P<x>[0-9]+),(?P<y>[0-9]+)|)'
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
dots = {(int(row.x), int(row.y)) for row in input_data if row.x}
folds = [(row.axis, int(row.val)) for row in input_data if row.axis]

for axis, val in folds[:1]:
    if axis == 'x':
        dots = {(x if x < val else 2*val-x, y) for x, y in dots}
    else:
        dots = {(x, y if y < val else 2*val-y) for x, y in dots}

answer = len(dots)
############################

# submit answer
puzzle.answer_a = answer
