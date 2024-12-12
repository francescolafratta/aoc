import os
import sys
from typing import List

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=7)


def check_equation(members: List[int], target: int, concat: bool) -> bool:
    solution_tree = []
    first, second, *rest = members
    starting_options = first + second, first * second
    if concat:
        concat_result = int(str(first) + str(second))
        starting_options += (concat_result,)
    solution_tree.append(list(starting_options))
    length = len(members)
    final_depth_level = length - 1
    current_depth = 0
    if final_depth_level > current_depth:
        for val in rest:
            changes = []
            for elem in solution_tree[current_depth]:
                options = val + elem, val * elem
                if concat:
                    concat_result = int(str(elem) + str(val))
                    options += (concat_result,)
                changes.extend([option for option in options if option <= target])
            solution_tree.append(changes)
            current_depth += 1
    final = solution_tree[-1]
    for elem in final:
        if elem == target:
            return True
    return False


calibration_result = 0
calibration_result_concat = 0
with open("input.txt", "r") as file:
    for line in file:
        before, separator, after = line.rstrip().partition(": ")
        target = int(before)
        equation_members = after.split(" ")
        equation_members = [int(member) for member in equation_members]
        is_equation_true = check_equation(equation_members, target, False)
        if is_equation_true:
            calibration_result += target
        else:
            is_equation_true_concat = check_equation(equation_members, target, True)
            if is_equation_true_concat:
                calibration_result_concat += target


print(calibration_result)
print(calibration_result + calibration_result_concat)
