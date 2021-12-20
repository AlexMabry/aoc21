import itertools

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=14)

# regex pattern
line_pattern = r'(?P<template>[A-Z]+$)|((?P<left>[A-Z]+) -> (?P<right>[A-Z]+))'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
template = input_data[0].template
rules = {row.left: row.right for row in input_data[1:]}

pair_counts = {pair: 0 for pair in rules.keys()}
letter_counts = {letter: 0 for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

for letter in template:
    letter_counts[letter] += 1

for pair in itertools.pairwise(template):
    pair_counts[''.join(pair)] += 1

for step in range(40):
    new_pair_counts = {pair: 0 for pair in rules.keys()}
    for pair, count in pair_counts.items():
        if count:
            inserted = rules[pair]
            letter_counts[inserted] += count
            new_pair_counts[pair[0]+inserted] += count
            new_pair_counts[inserted+pair[1]] += count
    pair_counts = {k: v for k, v in new_pair_counts.items()}

letter_counts = {k: v for k, v in letter_counts.items() if v}
ranked = sorted(letter_counts, key=letter_counts.get, reverse=True)
answer = letter_counts[ranked[0]] - letter_counts[ranked[-1]]
print(answer)
############################

# submit answer
puzzle.answer_b = answer
