import os
import sys
import itertools
from treelib import Node, Tree
target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=7)

def treefy(listy, target):
    grid = []
    first = listy[0]
    second = listy[1]
    grid.append([first + second, first * second])
    length = len(listy)
    final_depth_level = length - 1
    current_depth = 0
    if final_depth_level > current_depth:
        for index, val in enumerate(listy[2:]):
            changes = []
            for elem in grid[current_depth]:
                valsum = val + elem
                valmult = val * elem
                changes.extend([valsum, valmult])
            grid.append(changes)
            current_depth += 1
    final = grid[-1]
    for elem in final:
        if elem == target:
            return True
    return False

    
def treefy_concat(listy, target):
    grid = []
    first = listy[0]
    second = listy[1]
    grid.append([first+second, first*second, int(str(first)+str(second))])
    length = len(listy)
    final_depth_level = length - 1
    current_depth = 0
    if final_depth_level > current_depth:
        for index, val in enumerate(listy[2:]):
            changes = []
            for elem in grid[current_depth]:
                valsum = val + elem
                valmult = val*elem
                valconcat = int(str(elem) + str(val))
                changes.extend([valsum, valmult, valconcat])
            grid.append(changes)
            current_depth+=1
        final = grid[-1]
        for elem in final:
            if elem == target:
                return True
        return False

count = 0
count_concat = 0
with open("input.txt", "r") as file:
    for line in file:
        before, match, after = line.rstrip().partition(": ")
        new = [before] + after.split(" ")
        new = [int(elem) for elem in new]
        result = treefy(new[1:], new[0])
        if result:
            count+= new[0]
        else:
            result_concat = treefy_concat(new[1:], new[0])
            if result_concat:
                count_concat += new[0]


print(new)
print(count)
print(count+count_concat)


kappa = treefy([81, 40, 27], 3267)   
print(kappa)