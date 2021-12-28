from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations

from aocd import models

from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=18)

# format data
input_data = parse_data(puzzle.input_data, is_lines=True)

############################
snailfish = [eval(row) for row in input_data]

@dataclass
class SnailNode:
    val: int
    prev: SnailNode | None = None
    next: SnailNode | None = None

    def __str__(self):
        return f"{'' if self.prev else '-'}{self.val}{'' if self.next else '-'}"

    def magnitude(self):
        return self.val

@dataclass
class SnailPair:
    left: SnailNode | SnailPair
    right: SnailNode | SnailPair
    level: int

    def __str__(self):
        return f"[{self.left}, {self.right}]"

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

def should_explode(element: SnailNode | SnailPair):
    return element.level >= 4 if type(element) is SnailPair else False


def should_split(element: SnailNode | SnailPair):
    return element.val >= 10 if type(element) is SnailNode else False


def from_input(pair: list[int | list]):
    number = SnailNumber()
    number.top_pair = number.build_from_input(pair, 0)
    number.reduce()
    return number


def raise_level(pair: SnailPair):
    pair.level += 1
    for node in [pair.left, pair.right]:
        if node and type(node) is SnailPair:
            raise_level(node)


def add_numbers(a: SnailNumber, b: SnailNumber):
    result = SnailNumber()
    result.top_pair = SnailPair(a.top_pair, b.top_pair, -1)
    raise_level(result.top_pair)
    result.snail_head = a.snail_head
    a.snail_tail.next = b.snail_head
    b.snail_head.prev = a.snail_tail
    result.snail_tail = b.snail_tail
    result.reduce()
    return result


class SnailNumber:
    top_pair: SnailPair | None = None
    snail_head: SnailNode | None = None
    snail_tail: SnailNode | None = None

    def __str__(self):
        return f"{self.top_pair} {self.snail_tail}"

    def magnitude(self):
        return self.top_pair.magnitude()

    def list(self):
        node = self.snail_head
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return values

    def add_snail(self, val):
        snail = SnailNode(val, self.snail_tail)
        if not self.snail_head:
            self.snail_head = snail
            self.snail_tail = self.snail_head
        else:
            self.snail_tail.next = snail
            self.snail_tail = snail
        return snail

    def build_from_input(self, pair: list[int | list], level=0):
        left, right = [self.add_snail(val) if type(val) == int else self.build_from_input(val, level + 1) for val in pair]
        return SnailPair(left, right, level)

    def explode(self, snail: SnailPair):
        new_snail = SnailNode(0, snail.left.prev, snail.right.next)
        if new_snail.prev:
            new_snail.prev.val += snail.left.val
            new_snail.prev.next = new_snail
        else:
            self.snail_head = new_snail

        if new_snail.next:
            new_snail.next.val += snail.right.val
            new_snail.next.prev = new_snail
        else:
            self.snail_tail = new_snail

        return new_snail

    def reduce(self):
        reducing = True
        while reducing:
            reducing = self.reduce_pair(self.top_pair) or self.split_pair(self.top_pair)

    def split(self, node: SnailNode, level):
        left = SnailNode(node.val // 2)
        right = SnailNode(node.val - left.val, left)
        left.next = right

        if node.prev:
            node.prev.next = left
            left.prev = node.prev
        else:
            self.snail_head = left

        if node.next:
            node.next.prev = right
            right.next = node.next
        else:
            self.snail_tail = right

        return SnailPair(left, right, level)

    def split_pair(self, snail: SnailPair):
        if type(snail.left) is SnailNode:
            if should_split(snail.left):
                snail.left = self.split(snail.left, snail.level+1)
                return True
        else:
            if self.split_pair(snail.left):
                return True

        if type(snail.right) is SnailNode:
            if should_split(snail.right):
                snail.right = self.split(snail.right, snail.level+1)
                return True
        else:
            return self.split_pair(snail.right)
        return False

    def reduce_pair(self, snail: SnailPair):
        if type(snail.left) is SnailPair:
            if should_explode(snail.left):
                snail.left = self.explode(snail.left)
                return True
            else:
                if self.reduce_pair(snail.left):
                    return True

        if type(snail.right) is SnailPair:
            if should_explode(snail.right):
                snail.right = self.explode(snail.right)
                return True
            else:
                return self.reduce_pair(snail.right)
        return False


max_magnitude = 0
for a, b in permutations(snailfish, 2):
    total = add_numbers(from_input(a), from_input(b))
    max_magnitude = max(max_magnitude, total.magnitude())

answer = max_magnitude
############################
print(answer)

# submit answer
puzzle.answer_b = answer
