import os
import sys

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=4)

matrix = []

with open("input.txt", "r") as file:
    for line in file:
        line_list = []
        for elem in line:
            line_list.append(elem)
        line_list.pop()
        matrix.append(line_list)


def go_up(row, col, grid):
    if row == 0:
        return None
    return grid[row - 1][col]


def go_down(row, col, grid):
    if row == len(grid) - 1:
        return None
    return grid[row + 1][col]


def go_right(row, col, grid):
    if col == len(grid) - 1:
        return None
    return grid[row][col + 1]


def go_left(row, col, grid):
    if col == 0:
        return None
    return grid[row][col - 1]


def go_up_right(row, col, grid):
    if row == 0 or col == len(grid) - 1:
        return None
    return grid[row - 1][col + 1]


def go_up_left(row, col, grid):
    if row == 0 or col == 0:
        return None
    return grid[row - 1][col - 1]


def go_down_right(row, col, grid):
    if row == len(grid) - 1 or col == len(grid) - 1:
        return None
    return grid[row + 1][col + 1]


def go_down_left(row, col, grid):
    if col == 0 or row == len(grid) - 1:
        return None
    return grid[row + 1][col - 1]


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


char_search_dict = {0: "M", 1: "A", 2: "S"}
total_words = 0
total_xmas_words = 0
valid_permutations = [
    ["S", "M", "S", "M"],
    ["M", "S", "M", "S"],
    ["M", "M", "S", "S"],
    ["S", "S", "M", "M"],
]

for rindex, row in enumerate(matrix):
    for cindex, elem in enumerate(row):
        if elem == "X":
            up = can_search_up(rindex, cindex, matrix, 3)
            down = can_search_down(rindex, cindex, matrix, 3)
            right = can_search_right(rindex, cindex, matrix, 3)
            left = can_search_left(rindex, cindex, matrix, 3)
            upright = can_search_up_right(rindex, cindex, matrix, 3)
            upleft = can_search_up_left(rindex, cindex, matrix, 3)
            downright = can_search_down_right(rindex, cindex, matrix, 3)
            downleft = can_search_down_left(rindex, cindex, matrix, 3)

            if up:
                for i in range(3):
                    result = go_up(rindex - i, cindex, matrix)
                    if result != char_search_dict[i]:
                        break
                else:
                    total_words += 1

            if down:
                for i in range(3):
                    result = go_down(rindex + i, cindex, matrix)
                    if result != char_search_dict[i]:
                        break
                else:
                    total_words += 1

            if right:
                for i in range(3):
                    result = go_right(rindex, cindex + i, matrix)
                    if result != char_search_dict[i]:
                        break
                else:
                    total_words += 1

            if left:
                for i in range(3):
                    result = go_left(rindex, cindex - i, matrix)
                    if result != char_search_dict[i]:
                        break
                else:
                    total_words += 1

            if upright:
                for i in range(3):
                    result = go_up_right(rindex - i, cindex + i, matrix)
                    if result != char_search_dict[i]:
                        break
                else:
                    total_words += 1

            if upleft:
                for i in range(3):
                    result = go_up_left(rindex - i, cindex - i, matrix)
                    if result != char_search_dict[i]:
                        break
                else:
                    total_words += 1

            if downright:
                for i in range(3):
                    result = go_down_right(rindex + i, cindex + i, matrix)
                    if result != char_search_dict[i]:
                        break
                else:
                    total_words += 1

            if downleft:
                for i in range(3):
                    result = go_down_left(rindex + i, cindex - i, matrix)
                    if result != char_search_dict[i]:
                        break
                else:
                    total_words += 1
        elif elem == "A":
            upright = can_search_up_right(rindex, cindex, matrix, 1)
            upleft = can_search_up_left(rindex, cindex, matrix, 1)
            downright = can_search_down_right(rindex, cindex, matrix, 1)
            downleft = can_search_down_left(rindex, cindex, matrix, 1)

            if upright and upleft and downright and downleft:
                result_upright = go_up_right(rindex, cindex, matrix)
                result_upleft = go_up_left(rindex, cindex, matrix)
                result_downright = go_down_right(rindex, cindex, matrix)
                result_downleft = go_down_left(rindex, cindex, matrix)
                result_list = [
                    result_upright,
                    result_upleft,
                    result_downright,
                    result_downleft,
                ]
                if result_list in valid_permutations:
                    total_xmas_words += 1


print(total_words)
print(total_xmas_words)
