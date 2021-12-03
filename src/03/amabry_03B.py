from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=3)

# regex pattern
line_pattern = r'([01])([01])([01])([01])([01])([01])([01])([01])([01])([01])([01])([01])'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
def get_totals(ratings):
    totals = [0] * 12
    for rating in ratings:
        for pos in range(12):
            totals[pos] += (1 if rating[pos] == "1" else -1)
    return totals

def find_rating(ratings, most, least):
    pos = 0
    while len(ratings) > 1:
        totals = get_totals(ratings)
        target = most if totals[pos] >= 0 else least
        ratings = [rating for rating in ratings if rating[pos] == target]
        pos += 1
    return ratings[0]

oxygen = int("".join(find_rating(input_data, "1", "0")), 2)
co2 = int("".join(find_rating(input_data, "0", "1")), 2)
############################

# submit answer
puzzle.answer_b = oxygen * co2
