'''
--- Day 2.1: Red-Nosed Reports ---
Process the input file to have each report (row) as a list of integers.
Then compare the distance between each pair of consecutive integers in
the list to determine if the report is safe. Either increasing values 
or decreasing values are safe, so we repeat the process for the inverted
list => O(2n) => O(n)
'''

# Read input file
with open('input.txt') as f:
    lines = f.readlines()

def is_safe_part1(report: list, invert: bool) -> bool:
    report = report[::-1] if invert else report
    safe = True
    for idx in range(1, len(report)):
        safe = True if 1 <= report[idx] - report[idx-1] <= 3 else False
        if not safe:
            break

safe_reports = 0
for line in lines:
    report = list(map(int, line.rstrip().split()))
    safe = is_safe_part1(report, False) or is_safe_part1(report, True)

    safe_reports += safe

print(f'Safe reports: {safe_reports}')