import os
import sys

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=5)


def order_update(update):
    ordered_update = update.copy()
    update_set = set(update)
    for page in update:
        preceding_elements = set(ordering_rules[page])
        preceding_elements_in_update = update_set.intersection(preceding_elements)
        preceding_element_count = len(preceding_elements_in_update)
        ordered_update[preceding_element_count] = page
    return ordered_update


def is_ordered(update):
    length = len(update)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if update[j] in ordering_rules[update[i]]:
                return False
    return True


ordering_rules = {}
sum_middle_pages_in_ordered_updates = 0
sum_middle_pages_in_unordered_updates = 0

with open("input.txt", "r") as file:
    page_ordering_text = True
    for line in file:
        if line == "\n":
            page_ordering_text = False
            continue
        if page_ordering_text:
            preceding, following = line.rstrip().split("|")
            if following in ordering_rules:
                ordering_rules[following].append(preceding)
            else:
                ordering_rules[following] = [preceding]
        else:
            update = line.rstrip().split(",")
            length = len(update)
            middle_index = int(length / 2)
            ordered = is_ordered(update)

            if ordered:
                sum_middle_pages_in_ordered_updates += int(update[middle_index])
            else:
                ordered_update = order_update(update)
                sum_middle_pages_in_unordered_updates += int(
                    ordered_update[middle_index]
                )

print(sum_middle_pages_in_ordered_updates)
print(sum_middle_pages_in_unordered_updates)
