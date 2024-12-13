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

def shift_points(row1,col1,row2,col2):
    shiftrow = row1-row2
    shiftcol = col1-col2

    newrow1 = row1+shiftrow
    newcol1 = col1+shiftcol

    newrow2= row2-shiftrow
    newcol2 = col2-shiftcol

    p1 = newrow1,newcol1
    p2 = newrow2,newcol2

    return p1,p2
    

def get_antinodes(t1, t2, expanded):
    row1, col1 = t1
    row2, col2 = t2

    results = []
    if expanded:
        results.append(t1)
        results.append(t2)

    valid1 = True
    valid2 = True

    while valid1 or valid2:
        if not expanded:
            valid1 = False
            valid2 = False
        shifted_points = shift_points(row1,col1,row2,col2)
        newp1, newp2 = shifted_points
        row1, col1 = newp1
        row2, col2 = newp2
        validt1 = check_coords(newp1[0], newp1[1])
        validt2 = check_coords(newp2[0], newp2[1])

        if validt1:
            results.append(newp1)
        else:
            valid1 = False
        if validt2:
            results.append(newp2)
        else:
            valid2 = False

    return results

antinodes = []
antinodes_expanded =[]

for key in antennas:
    itert = itertools.combinations(antennas[key], 2)
    for t1, t2 in itert:
        mimi = get_antinodes(t1, t2, False)
        mimi_expand = get_antinodes(t1, t2, True)
        if mimi:
            antinodes.extend(mimi)
        if mimi_expand:
            antinodes_expanded.extend(mimi_expand)


unique_antinode_locations = set(antinodes)
print(len(unique_antinode_locations))

unique_antinode_expanded_locations = set(antinodes_expanded)
print(len(unique_antinode_expanded_locations))