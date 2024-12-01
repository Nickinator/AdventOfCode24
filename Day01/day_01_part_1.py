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

first_list.sort()
second_list.sort()

sum_of_distances = 0

for i in range(len(first_list)):
    sum_of_distances += abs(first_list[i] - second_list[i])

print(sum_of_distances)