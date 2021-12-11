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
SCORE = {']': 2, ')': 1, '}': 3, '>': 4}

scores = []
for line in input_data:
    q = deque()
    valid = True

    for ic, character in enumerate(line.chunks):
        if character in '[({<':
            q.append(character)
        elif CLOSES[q[-1]] == character:
            q.pop()
        else:
            valid = False
            break

    if valid:
        line_score = 0
        while q:
            line_score = line_score*5 + SCORE[CLOSES[q[-1]]]
            q.pop()
        scores.append(line_score)

sorted_scores = sorted(scores)
answer = sorted_scores[len(sorted_scores) // 2]
############################

# submit answer
puzzle.answer_b = answer
