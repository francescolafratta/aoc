import os
import sys

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=5)

precedence = {}
sum_middle_numbers = 0
sum_sorted = 0

def process_uncorrect(report):
    result = report.copy()
    myset = set(report)
    for elem in report:
        myset.remove(elem)
        preceds = set(precedence[elem])
        inter = myset.intersection(preceds)
        length = len(inter)
        result[length] = elem
        myset.add(elem)
    return result


with open("input.txt", "r") as file:
    page_ordering = True
    for line in file:
        if line == "\n":
            page_ordering = False
            continue
        if page_ordering:
            prev, cons = line.rstrip().split("|")
            if cons in precedence:
                precedence[cons].append(prev)
            else:
                precedence[cons] = [prev]
        else:
            stripped_line = line.rstrip().split(",")
            length = len(stripped_line)
            middle_index = int(length/2)
            correct_report = True
            for i in range(length - 1):
                for j in range(i + 1, length):
                    if stripped_line[j] in precedence[stripped_line[i]]:
                        correct_report = False
            if correct_report:
                sum_middle_numbers += int(stripped_line[middle_index])
            else:
                result = process_uncorrect(stripped_line)
                sum_sorted += int(result[middle_index])
                    
print(sum_middle_numbers)
print(sum_sorted)