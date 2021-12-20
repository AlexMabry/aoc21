from collections import defaultdict, deque

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=12)

# regex pattern
line_pattern = r'(?P<left>.*)-(?P<right>.*)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
caves = defaultdict(set)
for row in input_data:
    caves[row.left].add(row.right)
    caves[row.right].add(row.left)

q = deque(("start", edge) for edge in caves["start"])
complete_paths = set()
while q:
    path = q.pop()
    if path[-1] == "end":
        complete_paths.add(path)
    else:
        q.extend((*path, edge) for edge in caves[path[-1]] if edge.isupper() or edge not in path)

answer = len(complete_paths)
############################

# submit answer
puzzle.answer_a = answer
