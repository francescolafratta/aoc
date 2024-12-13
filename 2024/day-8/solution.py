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

    antinodes = []
    if expanded:
        antinodes.append(p1)
        antinodes.append(p2)

    continue_checking_p1 = True
    continue_checking_p2 = True

    while continue_checking_p1 or continue_checking_p2:
        if not expanded:
            continue_checking_p1 = False
            continue_checking_p2 = False
        p1, p2 = shift_points(p1, p2, shift)

        valid_shift_one = is_within_grid(p1)
        valid_shift_two = is_within_grid(p2)

        if valid_shift_one:
            antinodes.append(p1)
        else:
            continue_checking_p1 = False
        if valid_shift_two:
            antinodes.append(p2)
        else:
            continue_checking_p2 = False

    return antinodes


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
        couple_antinodes = get_antinodes(p1, p2, False)
        couple_antinodes_expanded = get_antinodes(p1, p2, True)
        if couple_antinodes:
            antinodes.extend(couple_antinodes)
        if couple_antinodes_expanded:
            antinodes_expanded.extend(couple_antinodes_expanded)


unique_antinode_locations = set(antinodes)
print(len(unique_antinode_locations))

unique_antinode_expanded_locations = set(antinodes_expanded)
print(len(unique_antinode_expanded_locations))
