import sys

with open('input.txt') as f:
    data = f.readlines()

data = [int(num) for num in data]

answer_1 = sum(data)

print(f'Answer One: {answer_1}')

freqs = set()
current_freq = 0

while True:
    for i in data:
        current_freq += i
        if current_freq in freqs:
            print(f'Answer Two: {current_freq}')
            sys.exit()
        else:
            freqs.add(current_freq)