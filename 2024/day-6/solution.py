import os
import sys
import itertools

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=6)

grid = []
cycler = itertools.cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])

with open("input.txt", "r") as file:
    for line in file:
        row = list(line.rstrip())
        grid.append(row)

def start_route(row, col, grid):
    dir = next(cycler)
    x_shift, y_shift = dir
    route = [(row, col)]
    while True:
        if row + x_shift < 0 or row + x_shift >= len(grid) or col + y_shift <0 or col + y_shift >= len(grid):
            break
        if grid[row+x_shift][col+y_shift] == "#":
            dir = next(cycler)
            x_shift, y_shift = dir
        row = row + x_shift
        col = col + y_shift
        route.append((row, col))
    return route



print(grid[0][1])
for row_index, row in enumerate(grid):
    for col_index, elem in enumerate(row):
        if elem == "^":
            routes = start_route(row_index, col_index, grid)
            print(len(set(routes)))