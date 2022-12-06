import csv

# A = rock
# B = paper
# C = scissors

# X = rock, 1pt
# Y = paper, 2pt
# Z = scissors, 3pt

# lose = 0pt
# draw = 3pt
# win = 6pt

score = 0

with open('rpc_strategy_guide.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row[1] == 'X':
            score = score + 1
        if row[1] == 'Y':
            score = score + 2
        if row[1] == 'Z':
            score = score + 3
        if row[0] == 'A' and row[1] == 'X':
            score = score + 3
        if row[0] == 'A' and row[1] == 'Y':
            score = score + 6
        if row[0] == 'A' and row[1] == 'Z':
            score = score + 0
        if row[0] == 'B' and row[1] == 'X':
            score = score + 0
        if row[0] == 'B' and row[1] == 'Y':
            score = score + 3
        if row[0] == 'B' and row[1] == 'Z':
            score = score + 6
        if row[0] == 'C' and row[1] == 'X':
            score = score + 6
        if row[0] == 'C' and row[1] == 'Y':
            score = score + 0
        if row[0] == 'C' and row[1] == 'Z':
            score = score + 3

print(score)
        






