import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util import read_input_file

data = read_input_file("Day02")

MIN_OFFSET = 1
MAX_OFFSET = 3

def is_safe(report: list[int]) -> bool:
    # check for offsets first
    for i in range(len(report) - 1):
        offset = abs(report[i] - report[i + 1])
        if offset < MIN_OFFSET or offset > MAX_OFFSET:
            return False

    # check for strictly ascending or descending order
    for i in range(len(report) - 1):
        if is_strictly_ascending(report) or is_strictly_descending(report):
            return True

    return False

def is_strictly_ascending(report: list[int]) -> bool:
    for i in range(len(report) - 1):
        if report[i] >= report[i + 1]:
            return False
    return True

def is_strictly_descending(report: list[int]) -> bool:
    for i in range(len(report) - 1):
        if report[i] <= report[i + 1]:
            return False
    return True

def problem_dampener(report: list[int]) -> bool:
    for i in range(len(report)):
        sub_report = report.copy()
        sub_report.pop(i)
        if is_safe(sub_report):
            return True
    return False   
    
safe_reports = 0
for line in data:
    report = [int(x) for x in line.split()]
    if problem_dampener(report):
        safe_reports += 1

print(safe_reports)