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


def execute_route(row, col, grid):
    length = len(grid)
    cycler = itertools.cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    x_shift, y_shift = next(cycler)
    route = [(row, col)]
    obstacles = {(-1, 0): [], (0, 1): [], (1, 0): [], (0, -1): []}
    loop = False
    while True:
        if (
            row + x_shift < 0
            or row + x_shift >= length
            or col + y_shift < 0
            or col + y_shift >= length
        ):
            break
        if grid[row + x_shift][col + y_shift] == "#":
            if (row + x_shift, col + y_shift) in obstacles[x_shift, y_shift]:
                loop = True
                break
            else:
                obstacles[x_shift, y_shift].append((row + x_shift, col + y_shift))
            x_shift, y_shift = next(cycler)
        else:
            row = row + x_shift
            col = col + y_shift
            route.append((row, col))
    return route, loop


for row_index, row in enumerate(grid):
    for col_index, elem in enumerate(row):
        if elem == "^":
            routes, is_loop = execute_route(row_index, col_index, grid)
            print(len(set(routes)))
            start_x, start_y = row_index, col_index

count_obstacle_loops = 0

for row_index, row in enumerate(grid):
    for col_index, elem in enumerate(row):
        if elem == ".":
            grid[row_index][col_index] = "#"
            routes, is_loop = execute_route(start_x, start_y, grid)
            if is_loop:
                count_obstacle_loops += 1
            grid[row_index][col_index] = "."

print(count_obstacle_loops)
