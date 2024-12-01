'''
--- Day 1: Historian hysteria ---
Process the input file to have the two vertical lists of integers in 
separate lists. Use the Counter class from the collections module to
count the number of occurrences of each integer in the left list. Then, 
simply iterate over the right list and record the similarity score 
(occurrence * integer). This avoids sorting the lists (O(nlogn)) or
a nested loop (O(n^2)) and is more efficient => O(n).
'''

# Read input file
with open('day1/input.txt') as f:
    lines = f.readlines()

# Parse input
list_l, list_r = [], []
for line in lines:
    l, r = line.rstrip().split('   ')
    list_l.append(int(l))
    list_r.append(int(r))

# Counter 
import collections
counter = collections.Counter(list_l)

# Find similarity score
scores = [counter[i] * i for i in list_r if i in counter]
print(f'Similarity score: {sum(score)}')