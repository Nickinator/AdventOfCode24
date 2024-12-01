import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path) as f:
    data = f.read().splitlines()

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