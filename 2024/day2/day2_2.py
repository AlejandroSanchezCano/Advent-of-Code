'''
--- Day 2.2: Red-Nosed Reports ---
Process the input file to have each report (row) as a list of integers.
Then compare the distance between each pair of consecutive integers in
the list. If the distance is too large (>3) or too little (<1), 
copies of the list without both compared integers are created and are
passed to the funciton from part 1 to determine if the remaining of the 
report is safe. This means we go to over the sequence of levels - 1 
twice in the worst case scenario. Plus, either increasing values or 
decreasing values are safe, so we repeat the process for the inverted
=> O(2n + 2(n-1)) => O(n).
'''

def is_safe_part1(report: list, invert: bool) -> bool:
    report = report[::-1] if invert else report
    safe = True
    for idx in range(1, len(report)):
        safe = True if 1 <= report[idx] - report[idx-1] <= 3 else False
        if not safe:
            break
    
    return safe

def is_safe_part2(report: list, invert: bool) -> bool:
    report = report[::-1] if invert else report
    safe = True
    for idx in range(1, len(report)):
        if not 1 <= report[idx] - report[idx-1] <= 3:
            without_idx = is_safe_part1(report[:idx] + report[idx + 1:], False)
            without_idx_1 = is_safe_part1(report[:idx - 1] + report[idx:], False)
            safe = without_idx or without_idx_1
    
    return safe

# Read input file
with open('input.txt') as f:
    lines = f.readlines()

safe_reports = 0
for line in lines:
    report = list(map(int, line.rstrip().split()))
    safe_reports += is_safe_part2(report, False) or is_safe_part2(report, True)

print(f'Safe reports: {safe_reports}')

