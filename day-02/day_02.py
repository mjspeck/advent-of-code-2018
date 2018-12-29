# Part 1: Count number of values with 2 of any letter and 
# values with 3 of any letter then multiply

import sys
import re
from collections import Counter

with open('input.txt') as f:
    data = f.readlines()

data = [i.rstrip('\n') for i in data]
data = [re.sub(r'[^a-zA-Z]', '', i) for i in data] # Just in case

num_twos = 0
num_threes = 0

for i in data:
    letter_vals = set(Counter(i).values())
    if 2 in letter_vals: num_twos += 1
    if 3 in letter_vals: num_threes += 1

print(f'Part 1 answer: {num_twos * num_threes}')

# Part 2:

data_lens = set([len(i) for i in data])
assert len(data_lens) == 1 # Just checking to make sure all data are the same length
data_len = data_lens.pop()

for i in range(data_len):
    vals = set()
    new_data = [j[:i] + j[i+1:] for j in data]
    for k in new_data:
        if k not in vals:
            vals.add(k)
        else:
            print(f'Part 2 answer: {k}')
            sys.exit(0)

else:
    print('No answer')
    sys.exit(1)
