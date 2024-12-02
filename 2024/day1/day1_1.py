'''
--- Day 1.1: Historian hysteria ---
Process the input file to have the two vertical lists of integers in 
separate lists, sort them, and calculate the difference between the
the integers at index i in the two lists => O(nlogn).
'''

# Read input file
with open('input.txt') as f:
    lines = f.readlines()

# Parse input
list_l, list_r = [], []
for line in lines:
    l, r = line.rstrip().split('   ')
    list_l.append(int(l))
    list_r.append(int(r))

# Sort lists
list_l.sort()
list_r.sort()

# Get difference
diffs = [abs(i-j) for i, j in zip(list_l, list_r)]

print(f'Difference: {sum(diffs)}')
