import os
import re
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util import read_input_file

data = read_input_file("Day03")
data = "".join(data)

mul_regex = r"mul\((\d+),(\d+)\)"
enable_regex = r"do\(\)"
disable_regex = r"don't\(\)"

regex = f"({mul_regex})|({enable_regex})|({disable_regex})"

matches = re.findall(regex, data)

total = 0
is_enabled = True
for match in matches:
    if match[1] and match[2] and is_enabled:
        total += int(match[1]) * int(match[2])
    elif match[3]:
        is_enabled = True
    elif match[4]:
        is_enabled = False

print(total)
