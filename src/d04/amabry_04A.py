import re

from aocd import models

from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=4)

# regex pattern
board_pattern = re.compile(r'([0-9]+)\s+([0-9]+)\s+([0-9]+)\s+([0-9]+)\s+([0-9]+)')

# format data
input_data = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=None)


def create_board(board_number):
    rows = range(board_number * 6 + 2, board_number * 6 + 7)
    return tuple(tuple(int(val) for val in board_pattern.search(input_data[row]).groups()) for row in rows)


def create_scorecard():
    return [[False for _ in range(5)] for __ in range(5)]


def find_number_location(b, number):
    for ix, row in enumerate(b):
        for iy, cell in enumerate(row):
            if cell == number:
                return ix, iy

    return None


def did_win(b):
    return any([all(row) for row in b]) or \
           any([all([b[ix][iy] for ix in range(5)]) for iy in range(5)]) or \
           all([b[i][i] for i in range(5)]) or \
           all([b[i][i] for i in range(4, -1, -1)])


def unmarked_numbers(board, marked):
    return [board[ix][iy] for ix, row in enumerate(marked) for iy, cell in enumerate(row) if not cell]


if __name__ == "__main__":
    numbers_drawn = [int(n) for n in input_data[0].split(",")]
    number_of_boards = len(input_data) // 6
    boards = [{"board": create_board(n), "marked": create_scorecard()} for n in range(number_of_boards)]

    for n in numbers_drawn:
        for b in boards:
            location = find_number_location(b["board"], n)
            if location:
                b["marked"][location[0]][location[1]] = True

            if did_win(b["marked"]):
                unmarked = unmarked_numbers(b["board"], b["marked"])
                puzzle.answer_a = sum(unmarked) * n
                exit(0)
