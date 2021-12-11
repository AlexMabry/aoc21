from collections import deque

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=10)

# regex pattern
line_pattern = r'(?P<chunks>.*)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
CLOSES = {'[': ']', '(': ')', '{': '}', '<': '>'}
SCORE = {']': 57, ')': 3, '}': 1197, '>': 25137}

total = 0
for line in input_data:
    q = deque()

    for ic, character in enumerate(line.chunks):
        if character in '[({<':
            q.append(character)
        elif CLOSES[q[-1]] == character:
            q.pop()
        else:
            total += SCORE[character]
            break
############################

# submit answer
puzzle.answer_a = total
