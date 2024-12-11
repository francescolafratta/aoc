import os
import sys
import itertools
from treelib import Node, Tree
target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=7)

def filter_by_depth(node, depth, target, tree):
    return tree.depth(node) == depth and node.data <= target

def filter_by_final_level(node, tree):
    return tree.depth() == tree.depth(node)

def treefy(listy, target):
    tree = Tree()
    tree.create_node(identifier = 0, data = 0)
    first = listy[0]
    second = listy[1]
    tree.create_node(identifier = 1, data = first+second, parent = 0)
    tree.create_node(identifier = 2, data = first*second, parent = 0)
    length = len(listy)
    final_depth_level = length - 1
    current_depth = tree.depth()
    if final_depth_level > current_depth:
        for index, val in enumerate(listy[2:]):
            filtered_nodes = tree.filter_nodes(lambda node: filter_by_depth(node, current_depth, target, tree))
            changes = []
            for node in filtered_nodes:
                parent = node.identifier
                data = val + node.data
                changes.append((parent,data))
                data_mult = val * node.data
                changes.append((parent, data_mult))
            for parent, data in changes:
                tree.create_node(parent = parent, data = data)
            current_depth += 1
    
    filtered_final = tree.filter_nodes(lambda node: filter_by_final_level(node, tree))
    for node in filtered_final:
        if node.data == target:
            return True
    return False


count = 0
with open("input.txt", "r") as file:
    for line in file:
        before, match, after = line.rstrip().partition(": ")
        new = [before] + after.split(" ")
        new = [int(elem) for elem in new]
        result = treefy(new[1:], new[0])
        if result:
            count+= new[0]

print(new)
print(count)



kappa = treefy([81, 40, 27], 3267)   
print(kappa)