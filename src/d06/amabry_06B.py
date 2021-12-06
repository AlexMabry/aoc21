from collections import deque

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=6)

# regex pattern
line_pattern = r'(?P<numbers>.*)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=True, regex=line_pattern)
fishes = deque([int(n) for n in input_data[0].numbers.split(",")])
max_days = 256

############################
def binomial_coeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res

weeks = max_days // 7 + 2
pascal_triangle = [[binomial_coeff(line, i) for i in range(0, line + 1)] for line in range(weeks+1)]

days = [0] * max_days
for week in range(weeks+1):
    current_day = week*7

    for val in pascal_triangle[week]:
        if current_day < max_days:
            days[current_day] += val
            current_day += 2

sum_days = sum(days)

fish_count = {
    1: sum_days - sum(days[-1:]),
    2: sum_days - sum(days[-2:]),
    3: sum_days - sum(days[-3:]),
    4: sum_days - sum(days[-4:]),
    5: sum_days - sum(days[-5:]),
}

total_fish = len(fishes)
for fish in fishes:
    total_fish += fish_count[fish]

############################

# submit answer
puzzle.answer_b = total_fish
