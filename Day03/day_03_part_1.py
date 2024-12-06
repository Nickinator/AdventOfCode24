import os
import re
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util import read_input_file

data = read_input_file("Day03")
data = "".join(data)

regex = r"mul\((\d+),(\d+)\)"

matches = re.findall(regex, data)

total = 0
for match in matches:
    total += int(match[0]) * int(match[1])

print(total)
