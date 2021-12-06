import re

from aocd import models

from src.utils import parse_data
from src.d04.amabry_04A import create_board, create_scorecard, find_number_location, did_win, unmarked_numbers

# create puzzle
puzzle = models.Puzzle(year=2021, day=4)

# regex pattern
board_pattern = re.compile(r'([0-9]+)\s+([0-9]+)\s+([0-9]+)\s+([0-9]+)\s+([0-9]+)')

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=None)

############################
numbers_drawn = [int(n) for n in input_data[0].split(",")]

number_of_boards = len(input_data) // 6
boards = [{"board": create_board(n), "marked": create_scorecard(), "won": False} for n in range(number_of_boards)]

print("Starting B")
winning_boards = 0
for n in numbers_drawn:
    print(n)
    for b in boards:
        if not b["won"]:
            location = find_number_location(b["board"], n)
            if location:
                b["marked"][location[0]][location[1]] = True

            b["won"] = did_win(b["marked"])
            winning_boards += 1 if b["won"] else 0
            print(winning_boards)
            if winning_boards == number_of_boards:
                unmarked = unmarked_numbers(b["board"], b["marked"])
                puzzle.answer_b = sum(unmarked) * n
                exit(0)

############################
