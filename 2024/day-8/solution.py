import os
import sys
import itertools

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=8)

antennas = {}
grid = []

with open("input.txt", "r") as file:
    for index, line in enumerate(file):
        stripped_line = list(line.rstrip())
        grid.append(stripped_line)
        for cindex, elem in enumerate(stripped_line):
            if elem != ".":
                if elem in antennas:
                    antennas[elem].append((index, cindex))
                else:
                    antennas[elem] = [(index, cindex)]

def check_coords(x, y):
    length = len(grid)
    if x < 0 or y < 0 or x >= length or y >=length:
        return False
    return True

def get_antinodes(t1, t2):
    row1, col1 = t1
    row2, col2 = t2

    shiftrow = row1-row2
    shiftcol = col1 - col2

    newrow1 = row1+shiftrow
    newcol1 = col1 +shiftcol
    
    newrow2 = row2-shiftrow
    newcol2 = col2-shiftcol

    validt1 = check_coords(newrow1, newcol1)
    validt2 = check_coords(newrow2, newcol2)

    results = []
    if validt1:
        results.append((newrow1, newcol1))
    if validt2:
        results.append((newrow2, newcol2))
    return results

antinodes = []

for key in antennas:
    itert = itertools.combinations(antennas[key], 2)
    for t1, t2 in itert:
        mimi = get_antinodes(t1, t2)
        if mimi:
            antinodes.extend(mimi)

unique_antinode_locations = set(antinodes)
print(len(unique_antinode_locations))