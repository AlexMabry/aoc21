import itertools
import re
from collections import defaultdict

import numpy as np
from aocd import models
from scipy.spatial import distance

from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=19)

# format data
input_data = parse_data(puzzle.input_data)

############################
def build_scanners(data):
    s_dict, s_num = defaultdict(list), None
    for row in data:
        if row.startswith('---'):
            s_num = int(re.search(r'[0-9]+', row)[0])
        elif len(row) > 0:
            s_dict[s_num].append(tuple(int(num) for num in row.split(',')))
    return s_dict

def scanner_directions():
    return (lambda x, y, z: (x, -z, y), lambda x, y, z: (x, z, -y), lambda x, y, z: (x, y, z),
            lambda x, y, z: (x, -y, -z), lambda x, y, z: (-x, z, y), lambda x, y, z: (-x, -z, -y),
            lambda x, y, z: (-x, -y, z), lambda x, y, z: (-x, y, -z), lambda x, y, z: (y, z, x),
            lambda x, y, z: (y, -z, -x), lambda x, y, z: (y, x, -z), lambda x, y, z: (y, -x, z),
            lambda x, y, z: (-y, -z, x), lambda x, y, z: (-y, z, -x), lambda x, y, z: (-y, x, z),
            lambda x, y, z: (-y, -x, -z), lambda x, y, z: (z, -y, x), lambda x, y, z: (z, y, -x),
            lambda x, y, z: (z, x, y), lambda x, y, z: (z, -x, -y), lambda x, y, z: (-z, y, x),
            lambda x, y, z: (-z, -y, -x), lambda x, y, z: (-z, x, -y), lambda x, y, z: (-z, -x, y))

scanners = build_scanners(input_data)
distances = {scanner: {distance.euclidean(a, b) for a, b in itertools.combinations(beacons, 2)} for scanner, beacons in
             scanners.items()}
in_common = {(a, b): common for a, b in itertools.combinations(scanners.keys(), 2) if
             len((common := distances[a] & distances[b])) >= 66}

all_beacons = set(scanners[0])
pairs_to_evaluate = set(in_common.keys())
scanners_to_check = set()
normalized = {0: scanners[0]}
scanner_location = {0: (0, 0, 0)}
scanner_a = 0

while pairs_to_evaluate:
    scanner_b = next((b if a == scanner_a else a for a, b in pairs_to_evaluate if scanner_a in (a, b)), None)
    if not scanner_b and not scanners_to_check:
        break
    elif not scanner_b:
        scanner_a = scanners_to_check.pop()
        continue
    else:
        pairs_to_evaluate.remove((min(scanner_a, scanner_b), max(scanner_a, scanner_b)))

    if scanner_b in scanner_location:
        continue
    else:
        scanners_to_check.add(scanner_b)

    common = in_common[(min(scanner_a, scanner_b), max(scanner_a, scanner_b))]

    matches_a = {dist: (a, b) for a, b in itertools.combinations(normalized[scanner_a], 2) if
                 (dist := distance.euclidean(a, b)) in common}
    points_a = {a for a, b in itertools.permutations(normalized[scanner_a], 2) if
                (dist := distance.euclidean(a, b)) in common}

    matches_b = {dist: (a, b) for a, b in itertools.combinations(scanners[scanner_b], 2) if
                 (dist := distance.euclidean(a, b)) in common}

    counts_b = {p: defaultdict(int) for p in points_a}
    for dist, (a1, a2) in matches_a.items():
        for b in matches_b[dist]:
            counts_b[a1][b] += 1
            counts_b[a2][b] += 1

    bizarro = {pa: next((pb for pb, val in count_b.items() if val > 1)) for pa, count_b in counts_b.items() if max(count_b.values()) > 1}

    for direction in scanner_directions():
        diff = [np.subtract(pa, direction(*pb)) for pa, pb in bizarro.items()]
        if np.all(diff == diff[0]):
            normalized[scanner_b] = {tuple(np.add(direction(*p), diff[0])) for p in scanners[scanner_b]}
            scanner_location[scanner_b] = diff[0]
            break

    all_beacons |= normalized[scanner_b]

answer = max(distance.cityblock(a, b) for a, b in itertools.combinations(scanner_location.values(), 2))
############################
print(answer)

# submit answer
puzzle.answer_b = answer
