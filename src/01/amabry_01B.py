from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=1)

# format data
input_data = parse_data(puzzle.input_data, is_numbers=True)
data_length = len(input_data)

increased = 0

previous = sum(input_data[0:3])
for index in range(data_length-2):
    current = sum(input_data[index:index+3])

    if current > previous:
        increased = increased + 1

    previous = current

# submit answer
puzzle.answer_b = increased
