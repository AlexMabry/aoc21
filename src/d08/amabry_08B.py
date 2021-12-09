from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=8)

# regex pattern
line_pattern = r'(?P<digits>[a-g ]+) \| (?P<output>[a-g ]+)'

# format data
entries = parse_data(puzzle.input_data, is_lines=True, is_numbers=False, regex=line_pattern)

############################
LETTERS = set('abcdefg')
OCCURRENCES = {4: 'e', 6: 'b', 9: 'f'}
LENGTHS = {2: '1', 3: '7', 4: '4', 7: '8'}

total = 0
for entry in entries:
    occurrences = {c: entry.digits.count(c) for c in LETTERS}
    signal_decode = {OCCURRENCES[cnt]: c for c, cnt in occurrences.items() if cnt in OCCURRENCES}
    digits = [set(d) for d in entry.digits.split(' ')]

    # Find 1, 7, 4, and 8
    digit_decode = {LENGTHS[d_len]: d for d in digits if (d_len := len(d)) in LENGTHS}

    # Find 0
    signal_decode['c'] = ''.join(digit_decode['1'] - {signal_decode['f']})
    signal_decode['a'] = ''.join(digit_decode['7'] - {signal_decode['f'], signal_decode['c']})
    digit_decode['0'] = next(d for d in digits if set(signal_decode.values()).issubset(d) and len(d) == 6)

    # Find 2, 3, 5, 6, 9
    signal_decode['g'] = ''.join(digit_decode['0'] - set(signal_decode.values()))
    signal_decode['d'] = ''.join(LETTERS - digit_decode['0'])
    digit_decode['2'] = set(signal_decode[c] for c in 'acdeg')
    digit_decode['3'] = set(signal_decode[c] for c in 'acdfg')
    digit_decode['5'] = set(signal_decode[c] for c in 'abdfg')
    digit_decode['6'] = set(signal_decode[c] for c in 'abdefg')
    digit_decode['9'] = set(signal_decode[c] for c in 'abcdfg')

    output_decode = {tuple(sorted(v)): k for k, v in digit_decode.items()}
    total += int(''.join([output_decode[tuple(sorted(o))] for o in entry.output.split(' ')]))
############################

# submit answer
# puzzle.answer_b = total
