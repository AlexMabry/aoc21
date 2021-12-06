from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=6)

# regex pattern
line_pattern = r'(?P<numbers>.*)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=True, regex=line_pattern)
fishes = [int(n) for n in input_data[0].numbers.split(",")]

############################
# Solve puzzle
print(fishes)

for day in range(80):
    new_fish = []
    for f, fish in enumerate(fishes):
        if fish == 0:
            new_fish.append(8)
            fishes[f] = 6
        else:
            fishes[f] -= 1

    fishes += new_fish

print(len(fishes))

############################

# submit answer
puzzle.answer_a = len(fishes)
