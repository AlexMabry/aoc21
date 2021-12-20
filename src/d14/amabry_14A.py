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

for step in range(10):
    elements = (rules[''.join(pair)] for pair in itertools.pairwise(template))
    template = ''.join((ct+ce for ct, ce in zip(template, elements))) + template[-1]

counts = {letter: count for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if (count := template.count(letter)) > 0}
ranked = sorted(counts, key=counts.get, reverse=True)
answer = counts[ranked[0]] - counts[ranked[-1]]
############################


# submit answer
puzzle.answer_a = answer
