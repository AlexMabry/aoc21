from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=8)

# regex pattern
line_pattern = r'(?P<digits>[a-g ]+) \| (?P<output>[a-g ]+)'

# format data
entries = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
easy_numbers = [True for entry in entries for digit in entry.output.split(' ') if len(digit) in [2, 3, 4, 7]]
############################

# submit answer
puzzle.answer_a = len(easy_numbers)
