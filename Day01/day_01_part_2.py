import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util import read_input_file

data = read_input_file("Day01")

first_list = []
second_list = []

for line in data:
    numbers = [int(x) for x in line.split()]
    first_list.append(numbers[0])
    second_list.append(numbers[1])

quantities = {}
for i in second_list:
    if i in quantities:
        quantities[i] += 1
    else:
        quantities[i] = 1

similarity_score = 0
for i in first_list:
    if i in quantities:
        similarity_score += i * quantities[i]

print(similarity_score)
