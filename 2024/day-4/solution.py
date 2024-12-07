import os
import sys

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=4)


def go_up(row, col, grid, qty):
    possible_move = can_move_up(row, col, grid, qty)
    moves = []
    if possible_move:
        for i in range(1, qty + 1):
            moves.append(grid[row - i][col])
    return moves


def go_down(row, col, grid, qty):
    possible_move = can_move_down(row, col, grid, qty)
    moves = []
    if possible_move:
        for i in range(1, qty + 1):
            moves.append(grid[row + i][col])
    return moves


def go_right(row, col, grid, qty):
    possible_move = can_move_right(row, col, grid, qty)
    moves = []
    if possible_move:
        for i in range(1, qty + 1):
            moves.append(grid[row][col + i])
    return moves


def go_left(row, col, grid, qty):
    possible_move = can_move_left(row, col, grid, qty)
    moves = []
    if possible_move:
        for i in range(1, qty + 1):
            moves.append(grid[row][col - i])
    return moves


def go_up_right(row, col, grid, qty):
    possible_move = can_move_up_right(row, col, grid, qty)
    moves = []
    if possible_move:
        for i in range(1, qty + 1):
            moves.append(grid[row - i][col + i])
    return moves


def go_up_left(row, col, grid, qty):
    possible_move = can_move_up_left(row, col, grid, qty)
    moves = []
    if possible_move:
        for i in range(1, qty + 1):
            moves.append(grid[row - i][col - i])
    return moves


def go_down_right(row, col, grid, qty):
    possible_move = can_move_down_right(row, col, grid, qty)
    moves = []
    if possible_move:
        for i in range(1, qty + 1):
            moves.append(grid[row + i][col + i])
    return moves


def go_down_left(row, col, grid, qty):
    possible_move = can_move_down_left(row, col, grid, qty)
    moves = []
    if possible_move:
        for i in range(1, qty + 1):
            moves.append(grid[row + i][col - i])
    return moves


def can_move_up(row, col, grid, qty):
    if row < qty:
        return False
    return True


def can_move_down(row, col, grid, qty):
    if len(grid) - row < qty + 1:
        return False
    return True


def can_move_right(row, col, grid, qty):
    if len(grid) - col < qty + 1:
        return False
    return True


def can_move_left(row, col, grid, qty):
    if col < qty:
        return False
    return True


def can_move_up_right(row, col, grid, qty):
    if row < qty or len(grid) - col < qty + 1:
        return False
    return True


def can_move_up_left(row, col, grid, qty):
    if row < qty or col < qty:
        return False
    return True


def can_move_down_right(row, col, grid, qty):
    if len(grid) - col < qty + 1 or len(grid) - row < qty + 1:
        return False
    return True


def can_move_down_left(row, col, grid, qty):
    if col < qty or len(grid) - row < qty + 1:
        return False
    return True


grid = []

with open("input.txt", "r") as file:
    for line in file:
        row = list(line.rstrip())
        grid.append(row)


mas_target = ["M", "A", "S"]
permutation_targets = [
    ["S", "M", "S", "M"],
    ["M", "S", "M", "S"],
    ["M", "M", "S", "S"],
    ["S", "S", "M", "M"],
]
xmas_words = 0
xshape_words = 0


for row_index, row in enumerate(grid):
    for col_index, elem in enumerate(row):
        if elem == "X":
            up = go_up(row_index, col_index, grid, 3)
            down = go_down(row_index, col_index, grid, 3)
            right = go_right(row_index, col_index, grid, 3)
            left = go_left(row_index, col_index, grid, 3)
            upright = go_up_right(row_index, col_index, grid, 3)
            upleft = go_up_left(row_index, col_index, grid, 3)
            downright = go_down_right(row_index, col_index, grid, 3)
            downleft = go_down_left(row_index, col_index, grid, 3)

            if up == mas_target:
                xmas_words += 1

            if down == mas_target:
                xmas_words += 1

            if right == mas_target:
                xmas_words += 1

            if left == mas_target:
                xmas_words += 1

            if upright == mas_target:
                xmas_words += 1

            if upleft == mas_target:
                xmas_words += 1

            if downright == mas_target:
                xmas_words += 1

            if downleft == mas_target:
                xmas_words += 1
        elif elem == "A":
            upright = go_up_right(row_index, col_index, grid, 1)
            upleft = go_up_left(row_index, col_index, grid, 1)
            downright = go_down_right(row_index, col_index, grid, 1)
            downleft = go_down_left(row_index, col_index, grid, 1)

            if upright and upleft and downright and downleft:
                move_results = upright + upleft + downright + downleft
                if move_results in permutation_targets:
                    xshape_words += 1


print(xmas_words)
print(xshape_words)
