import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util import read_input_file

data = read_input_file("Day04")
data = [list(line) for line in data]

rows = len(data)
cols = len(data[0])

count = 0
for r in range(rows):
    for c in range(cols):
        # left to right
            if c + 3 < cols and data[r][c] == 'X' and data[r][c + 1] == 'M' and data[r][c + 2] == 'A' and data[r][c + 3] == 'S':
                count += 1

        # right to left
            if c - 3 >= 0 and data[r][c] == 'X' and data[r][c - 1] == 'M' and data[r][c - 2] == 'A' and data[r][c - 3] == 'S':
                count += 1

        # top to bottom
            if r + 3 < rows and data[r][c] == 'X' and data[r + 1][c] == 'M' and data[r + 2][c] == 'A' and data[r + 3][c] == 'S':
                count += 1

        # bottom to top
            if r - 3 >= 0 and data[r][c] == 'X' and data[r - 1][c] == 'M' and data[r - 2][c] == 'A' and data[r - 3][c] == 'S':
                count += 1

        # top left to bottom right
            if r + 3 < rows and c + 3 < cols and data[r][c] == 'X' and data[r + 1][c + 1] == 'M' and data[r + 2][c + 2] == 'A' and data[r + 3][c + 3] == 'S':
                count += 1

        # bottom right to top left
            if r - 3 >= 0 and c - 3 >= 0 and data[r][c] == 'X' and data[r - 1][c - 1] == 'M' and data[r - 2][c - 2] == 'A' and data[r - 3][c - 3] == 'S':
                count += 1

        # top right to bottom left
            if r + 3 < rows and c - 3 >= 0 and data[r][c] == 'X' and data[r + 1][c - 1] == 'M' and data[r + 2][c - 2] == 'A' and data[r + 3][c - 3] == 'S':
                count += 1

        # bottom left to top right
            if r - 3 >= 0 and c + 3 < cols and data[r][c] == 'X' and data[r - 1][c + 1] == 'M' and data[r - 2][c + 2] == 'A' and data[r - 3][c + 3] == 'S':
                count += 1

print(count)
