import os
import sys
from typing import List

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=2)


def validate_report(report: List[int]) -> bool:
    report_length = len(report)

    for i in range(report_length - 1):
        diff = report[i] - report[i + 1]
        abs_diff = abs(diff)
        if i == 0:
            first_diff = diff

        if abs_diff < 1 or abs_diff > 3:
            return False
        if i > 0:
            if diff * first_diff < 0:
                return False

    return True


def validate_report_with_tolerance(report: List[int]) -> bool:
    result = validate_report(report)
    if result:
        return True
    else:
        report_length = len(report)
        for i in range(report_length):
            elem = report.pop(i)
            elim_result = validate_report(report)
            if elim_result:
                return True
            else:
                report.insert(i, elem)
        return False


valid_reports = 0
valid_reports_with_tolerance = 0
with open("input.txt", "r") as file:
    for line in file:
        report = line.rstrip().split()
        report = [int(elem) for elem in report]
        if validate_report(report):
            valid_reports += 1
        if validate_report_with_tolerance(report):
            valid_reports_with_tolerance += 1

print(valid_reports)
print(valid_reports_with_tolerance)
