import math
from collections import deque

from aocd import models

from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=9)

# regex pattern
line_pattern = r'(?P<numbers>.*)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
size = len(input_data)
grid = [[int(num) for num in row.numbers] for row in input_data]
heights = {(ix, iy): grid[ix][iy] for ix in range(size) for iy in range(size)}

def axis_range(c):
    return range(max(0, c - 1), min(size, c + 2))

def neighbor_range(p):
    return ((ix, iy) for ix in axis_range(p[0]) for iy in axis_range(p[1]))

def neighbor_values(p):
    return (heights[np] for np in neighbor_range(p) if np != p)

def close_neighbors(p):
    return (np for np in neighbor_range(p) if np[0] == p[0] or np[1] == p[1])

def get_basin(point):
    basin = set()
    q = deque([point])
    while q:
        p = q.pop()
        basin.add(p)
        q.extend((np for np in close_neighbors(p) if heights[np] < 9 and np not in basin))

    return basin

low_points = (p for p, h in heights.items() if h < min(neighbor_values(p)))
basins = sorted((len(get_basin(lp)) for lp in low_points), reverse=True)

answer = math.prod(basins[0:3])
############################

# submit answer
puzzle.answer_b = answer
