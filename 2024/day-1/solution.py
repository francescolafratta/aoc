import os
import sys

target_dir = os.path.abspath("../../")
sys.path.insert(0, target_dir)
import input

if not (os.path.exists("input.txt")):
    input.save_input(year=2024, day=1)

left = []
right = []
left_counter = {}
right_counter = {}
with open("input.txt", "r") as file:
    for line in file:
        l, r = line.rstrip().split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()
distance = 0

for left_elem, right_elem in zip(left, right):
    distance += abs(left_elem - right_elem)

    if left_elem in left_counter:
        left_counter[left_elem] += 1
    else:
        left_counter[left_elem] = 1

    if right_elem in right_counter:
        right_counter[right_elem] += 1
    else:
        right_counter[right_elem] = 1

print(distance)

similarity_score = 0
for key, val in left_counter.items():
    similarity_score += key * val * right_counter.get(key, 0)

print(similarity_score)
