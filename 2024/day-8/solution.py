import itertools
import os
import sys
from dataclasses import dataclass
from typing import List, Tuple

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=8)


@dataclass(frozen=True)
class Point:
    row: int
    col: int


def is_within_grid(p: Point) -> bool:
    if p.row < 0 or p.col < 0 or p.row >= length or p.col >= length:
        return False
    return True


def get_shift(p1: Point, p2: Point) -> Point:
    return Point(p1.row - p2.row, p1.col - p2.col)


def shift_points(p1: Point, p2: Point, shift: Point) -> Tuple[Point, Point]:
    p1 = Point(p1.row + shift.row, p1.col + shift.col)
    p2 = Point(p2.row - shift.row, p2.col - shift.col)
    return p1, p2


def get_antinodes(p1: Point, p2: Point, expanded: bool) -> List[Point]:
    shift = get_shift(p1, p2)

    results = []
    if expanded:
        results.append(p1)
        results.append(p2)

    within1 = True
    within2 = True

    while within1 or within2:
        if not expanded:
            within1 = False
            within2 = False
        p1, p2 = shift_points(p1, p2, shift)

        validt1 = is_within_grid(p1)
        validt2 = is_within_grid(p2)

        if validt1:
            results.append(p1)
        else:
            within1 = False
        if validt2:
            results.append(p2)
        else:
            within2 = False

    return results


antennas = {}
grid = []

with open("input.txt", "r") as file:
    for row, line in enumerate(file):
        stripped_line = list(line.rstrip())
        grid.append(stripped_line)
        for col, elem in enumerate(stripped_line):
            if elem != ".":
                if elem in antennas:
                    antennas[elem].append(Point(row, col))
                else:
                    antennas[elem] = [Point(row, col)]

length = len(grid)


antinodes = []
antinodes_expanded = []

for key in antennas:
    iterator = itertools.combinations(antennas[key], 2)
    for p1, p2 in iterator:
        mimi = get_antinodes(p1, p2, False)
        mimi_expand = get_antinodes(p1, p2, True)
        if mimi:
            antinodes.extend(mimi)
        if mimi_expand:
            antinodes_expanded.extend(mimi_expand)


unique_antinode_locations = set(antinodes)
print(len(unique_antinode_locations))

unique_antinode_expanded_locations = set(antinodes_expanded)
print(len(unique_antinode_expanded_locations))
