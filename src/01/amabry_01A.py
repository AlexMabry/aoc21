from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=1)

# format data
input_data = parse_data(puzzle.input_data, is_numbers=True)

increased = 0

previous = input_data[0]
for number in input_data:
    if number > previous:
        increased = increased + 1

    previous = number

# submit answer
puzzle.answer_a = increased
