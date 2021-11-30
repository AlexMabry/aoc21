import re
from types import SimpleNamespace


def parse_data(puzzle, is_lines: bool = True, is_numbers: bool = False, regex=None):
    lines = puzzle.input_data.splitlines()
    if regex:
        pattern = re.compile(regex)
        if pattern.groupindex.keys():
            return [SimpleNamespace(**pattern.search(item).groupdict()) for item in lines]
        else:
            return [pattern.search(item).groups() for item in lines]

    if is_numbers:
        return [int(n) for n in lines]
    elif is_lines:
        return lines
    else:
        return puzzle.input_data
