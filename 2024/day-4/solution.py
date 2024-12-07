import os
import sys

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=4)


def go_up(row, col, grid, qty):
    check_result = can_search_up(row, col, grid, qty)
    result = []
    if check_result:
        for i in range(1, qty + 1):
            result.append(grid[row - i][col])
    return result


def go_down(row, col, grid, qty):
    check_result = can_search_down(row, col, grid, qty)
    result = []
    if check_result:
        for i in range(1, qty + 1):
            result.append(grid[row + i][col])
    return result


def go_right(row, col, grid, qty):
    check_result = can_search_right(row, col, grid, qty)
    result = []
    if check_result:
        for i in range(1, qty + 1):
            result.append(grid[row][col + i])
    return result


def go_left(row, col, grid, qty):
    check_result = can_search_left(row, col, grid, qty)
    result = []
    if check_result:
        for i in range(1, qty + 1):
            result.append(grid[row][col - i])
    return result


def go_up_right(row, col, grid, qty):
    check_result = can_search_up_right(row, col, grid, qty)
    result = []
    if check_result:
        for i in range(1, qty + 1):
            result.append(grid[row - i][col + i])
    return result


def go_up_left(row, col, grid, qty):
    check_result = can_search_up_left(row, col, grid, qty)
    result = []
    if check_result:
        for i in range(1, qty + 1):
            result.append(grid[row - i][col - i])
    return result


def go_down_right(row, col, grid, qty):
    check_result = can_search_down_right(row, col, grid, qty)
    result = []
    if check_result:
        for i in range(1, qty + 1):
            result.append(grid[row + i][col + i])
    return result


def go_down_left(row, col, grid, qty):
    check_result = can_search_down_left(row, col, grid, qty)
    result = []
    if check_result:
        for i in range(1, qty + 1):
            result.append(grid[row + i][col - i])
    return result


def can_search_up(row, col, grid, qty):
    if row < qty:
        return False
    return True


def can_search_down(row, col, grid, qty):
    if len(grid) - row < qty + 1:
        return False
    return True


def can_search_right(row, col, grid, qty):
    if len(grid) - col < qty + 1:
        return False
    return True


def can_search_left(row, col, grid, qty):
    if col < qty:
        return False
    return True


def can_search_up_right(row, col, grid, qty):
    if row < qty or len(grid) - col < qty + 1:
        return False
    return True


def can_search_up_left(row, col, grid, qty):
    if row < qty or col < qty:
        return False
    return True


def can_search_down_right(row, col, grid, qty):
    if len(grid) - col < qty + 1 or len(grid) - row < qty + 1:
        return False
    return True


def can_search_down_left(row, col, grid, qty):
    if col < qty or len(grid) - row < qty + 1:
        return False
    return True


grid = []

with open("input.txt", "r") as file:
    for line in file:
        row = list(line.rstrip())
        grid.append(row)


valid_target = ["M", "A", "S"]
total_words = 0
total_xmas_words = 0
valid_permutations = [
    ["S", "M", "S", "M"],
    ["M", "S", "M", "S"],
    ["M", "M", "S", "S"],
    ["S", "S", "M", "M"],
]

for rindex, row in enumerate(grid):
    for cindex, elem in enumerate(row):
        if elem == "X":
            up = go_up(rindex, cindex, grid, 3)
            down = go_down(rindex, cindex, grid, 3)
            right = go_right(rindex, cindex, grid, 3)
            left = go_left(rindex, cindex, grid, 3)
            upright = go_up_right(rindex, cindex, grid, 3)
            upleft = go_up_left(rindex, cindex, grid, 3)
            downright = go_down_right(rindex, cindex, grid, 3)
            downleft = go_down_left(rindex, cindex, grid, 3)

            if up == valid_target:
                total_words += 1

            if down == valid_target:
                total_words += 1

            if right == valid_target:
                total_words += 1

            if left == valid_target:
                total_words += 1

            if upright == valid_target:
                total_words += 1

            if upleft == valid_target:
                total_words += 1

            if downright == valid_target:
                total_words += 1

            if downleft == valid_target:
                total_words += 1
        elif elem == "A":
            upright = go_up_right(rindex, cindex, grid, 1)
            upleft = go_up_left(rindex, cindex, grid, 1)
            downright = go_down_right(rindex, cindex, grid, 1)
            downleft = go_down_left(rindex, cindex, grid, 1)

            if upright and upleft and downright and downleft:
                result_list = upright + upleft + downright + downleft
                if result_list in valid_permutations:
                    total_xmas_words += 1


print(total_words)
print(total_xmas_words)
