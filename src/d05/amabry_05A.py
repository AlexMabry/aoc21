from collections import defaultdict
from dataclasses import dataclass

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=5)

# regex pattern
line_pattern = r'(?P<x1>[0-9]+),(?P<y1>[0-9]+) -> (?P<x2>[0-9]+),(?P<y2>[0-9]+)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
@dataclass
class Point:
    x: int
    y: int


lines = [(Point(int(p.x1), int(p.y1)), Point(int(p.x2), int(p.y2))) for p in input_data]

points = defaultdict(int)
for p1, p2 in lines:
    if p1.x == p2.x:  # vert
        for iy in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
            points[(p1.x, iy)] += 1
    elif p1.y == p2.y:  # horz
        for ix in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
            points[(ix, p1.y)] += 1

answer = len([val for val in points.values() if val > 1])
print(answer)

############################

# submit answer
puzzle.answer_a = answer
