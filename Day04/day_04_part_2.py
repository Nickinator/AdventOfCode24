import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util import read_input_file

data = read_input_file("Day04")
data = [list(line) for line in data]

rows = len(data)
cols = len(data[0])

def check_bottom_left_to_top_right(row, col) -> bool:
    if data[row + 1][col - 1] == 'M' and data[row - 1][col + 1] == 'S': 
        return True
    
    if data[row + 1][col - 1] == 'S' and data[row - 1][col + 1] == 'M': 
        return True

    return False

def check_bottom_right_to_top_left(row, col) -> bool:
    if data[row + 1][col + 1] == 'M' and data[row - 1][col - 1] == 'S': 
        return True
    
    if data[row + 1][col + 1] == 'S' and data[row - 1][col - 1] == 'M': 
        return True

    return False

count = 0
for r in range(rows):
    for c in range(cols):
        if data[r][c] == 'A' and r > 0 and r < rows - 1 and c > 0 and c < cols - 1:
            if check_bottom_left_to_top_right(r, c) and check_bottom_right_to_top_left(r, c):
                count += 1                

print(count)
