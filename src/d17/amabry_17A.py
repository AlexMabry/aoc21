from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=17)

# regex pattern
line_pattern = r'target area: x=(?P<x1>[0-9]+)..(?P<x2>[0-9]+), y=(?P<y1>[-0-9]+)..(?P<y2>[-0-9]+)'

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
x_bounds = int(input_data[0].x1), int(input_data[0].x2)
y_bounds = int(input_data[0].y1), int(input_data[0].y2)

def is_past(pos):
    return pos[0] > x_bounds[1] or pos[1] < y_bounds[0]

def in_bounds(pos):
    return x_bounds[0] <= pos[0] <= x_bounds[1] and y_bounds[0] <= pos[1] <= y_bounds[1]

def update_position(pos, vel):
    return pos[0] + vel[0], pos[1] + vel[1]

def update_velocity(vel):
    drag = -1 if vel[0] > 0 else 1 if vel[0] < 0 else 0
    return vel[0] + drag, vel[1] - 1

max_height = 0
for ix in range(30):
    for iy in range(100):
        position = (0, 0)
        velocity = (ix, iy)
        this_max_height = 0

        while not is_past(position):
            this_max_height = max(this_max_height, position[1])
            position = update_position(position, velocity)
            velocity = update_velocity(velocity)

            if in_bounds(position):
                max_height = max(max_height, this_max_height)

answer = max_height
############################
print(answer)

# submit answer
puzzle.answer_a = answer
