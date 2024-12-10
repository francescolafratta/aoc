import itertools
import os
import sys

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=6)

grid = []

with open("input.txt", "r") as file:
    for line in file:
        row = list(line.rstrip())
        grid.append(row)


def start_route(row, col, grid):
    cycler = itertools.cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    dir = next(cycler)
    x_shift, y_shift = dir
    route = [(row, col)]
    obstacles = {(-1, 0): [], (0, 1): [], (1, 0): [], (0, -1): []}
    loop = False
    while True:
        if (
            row + x_shift < 0
            or row + x_shift >= len(grid)
            or col + y_shift < 0
            or col + y_shift >= len(grid)
        ):
            break
        if grid[row + x_shift][col + y_shift] == "#":
            if (row + x_shift, col + y_shift) in obstacles[dir]:
                loop = True
                break
            else:
                obstacles[dir].append((row + x_shift, col + y_shift))
            dir = next(cycler)
            x_shift, y_shift = dir
        else:
            row = row + x_shift
            col = col + y_shift
            route.append((row, col))
    return route, loop


for row_index, row in enumerate(grid):
    for col_index, elem in enumerate(row):
        if elem == "^":
            routes, loopt = start_route(row_index, col_index, grid)
            print(len(set(routes)))
            print(loopt)
            sentinel = row_index, col_index

count = 0

for row_index, row in enumerate(grid):
    for col_index, elem in enumerate(row):
        if elem == ".":
            grid[row_index][col_index] = "#"
            routesadd, loopadd = start_route(sentinel[0], sentinel[1], grid)
            if loopadd:
                count += 1
            grid[row_index][col_index] = "."

print(count)
