'''
--- Day 3.1: Mull it over ---
Process the input file as a single string and use regex to find all
pairs of integers of the form mul(a, b) and multiply them to get the
result => O(n)
'''

# Read input file
with open('input.txt') as f:
    memory = f.read()

import re
result = 0
for a, b in re.findall(r'mul\((\d+),(\d+)\)', memory):
    a, b = int(a), int(b)
    result += a * b

print(f'Result: {result}')