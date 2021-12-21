import math
from collections import deque

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=15)

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=None)

############################
positions = {(x, y): int(num) for y, row in enumerate(input_data) for x, num in enumerate(row)}
size = len(input_data)

def axis_range(c):
    return range(max(0, c - 1), min(size, c + 2))

def neighbor_range(p):
    return ((ix, iy) for ix in axis_range(p[0]) for iy in axis_range(p[1]))

def close_neighbors(p):
    return (np for np in neighbor_range(p) if np != p and (np[0] == p[0] or np[1] == p[1]))

START = (0, 0)
END = (size-1, size-1)

path_home = {(x, y): math.inf for y in range(size) for x in range(size)}
path_home[START] = 0

q = deque([START])
while q:
    point = q.popleft()

    for n in close_neighbors(point):
        risk = positions[n] + path_home[point]
        if risk < path_home[n]:
            path_home[n] = risk
            q.append(n)

answer = path_home[END]
############################
print(answer)

# submit answer
puzzle.answer_a = answer
