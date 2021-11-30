from aocd import models
from ..utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=8)

# regex pattern
line_pattern = r'(?P<group_name>.*)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
# Solve puzzle
print(input_data)

answer_to_submit = None
############################

# submit answer
puzzle.answer_a = answer_to_submit
