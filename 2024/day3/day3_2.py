'''
--- Day 3.2: Mull it over ---
Process the input file as a single string and iterate over each
character to search for the pattern mul(a, b), "do()" or "don't()"
and act accordingly => O(n).
This becomes as simple as part 1 if we use regex: 
r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
'''


# Read input file
with open('input.txt') as f:
    memory = f.read()

def valid_instruction(idx):
    a, b = '', ''
    counter = 4
    comma = False
    if memory[idx:idx + 4] != 'mul(':
        return False
    while True:
        if memory[idx + counter].isdigit():
            counter += 1
            if not comma:
                a += memory[idx + counter - 1]
            else:
                b += memory[idx + counter - 1]
        elif memory[idx + counter] == ',' and not comma and a:
            counter += 1
            comma = True
        elif memory[idx + counter] == ')' and comma and b:
            return int(a), int(b)
        else:
            return False
        
def do_dont(idx):
    if memory[idx:idx + 4] == 'do()':
        return True
    elif memory[idx:idx + 7] == "don't()":
        return False
    else:
        return None

result = 0 
allows = True
for idx in range(len(memory)):
    # Process instruction
    nums = valid_instruction(idx)
    if nums and allows:
        result += nums[0] * nums[1]

    # Monitor state
    abled = do_dont(idx) 
    if abled is not None:
        allows = abled

print(f'Result: {result}') 