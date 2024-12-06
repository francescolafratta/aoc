import os
import re
import sys
from typing import List

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=3)

with open("input.txt", "r") as file:
    memory_string = file.read()


def get_distance_from_closest(lst: List[int], target: int) -> int:
    """
    Returns distance between the target value and the largest element
    in the list that is still smaller than the target.
    Returns -1 if no such element is found.
    Assumes the list is sorted and contains positive numbers only.
    """
    for index, elem in enumerate(lst):
        if elem > target:
            if index == 0:
                return -1
            else:
                return target - lst[index - 1]
    return target - lst[index]


do_pattern = r"do[(][)]"
dont_pattern = r"don't[(][)]"
do_end_indexes = []
dont_end_indexes = []

for elem in re.finditer(do_pattern, memory_string):
    do_end_indexes.append(elem.end() - 1)
for elem in re.finditer(dont_pattern, memory_string):
    dont_end_indexes.append(elem.end() - 1)

mul_pattern = r"mul[(][0-9]{1,3},[0-9]{1,3}[)]"
total = 0
enabled_total = 0

for elem in re.finditer(mul_pattern, memory_string):
    mul_text = elem.group()
    mul_start_index = elem.start()

    mul_text_stripped = mul_text.lstrip("mul(").rstrip(")")
    first, second = mul_text_stripped.split(",")
    product = int(first) * int(second)
    total += product

    dist_do = get_distance_from_closest(do_end_indexes, mul_start_index)
    dist_dont = get_distance_from_closest(dont_end_indexes, mul_start_index)
    if dist_dont < 0:
        enabled_total += product
    elif dist_do > 0:
        if dist_do < dist_dont:
            enabled_total += product

print(total)
print(enabled_total)
