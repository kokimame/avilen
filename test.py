import csv

# Read .txt file. Use the CSV module to do stripping automatically
with open('input.txt', 'r') as f:
    lines = [line[0] for line in csv.reader(f)]

m = int(lines[-1])
# Pairs of i (integer) and s (string)
i_s_pairs = []
for i_s in lines[:-1]:
    assert ':' in i_s
    i, s = i_s.split(':')
    i_s_pairs.append((int(i), s))

# Sort the pairs to smaller i first
i_s_pairs.sort(key=lambda x: x[0])

output = ''
for i, s in i_s_pairs:
    if m % i == 0:
        output += s
# If some text is appended to the output
if output:
    print(output)
# Otherwise, print the m
else:
    print(m)


