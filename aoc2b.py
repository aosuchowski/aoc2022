import csv

# A = rock, 1pt
# B = paper, 2pt
# C = scissors, 3pt

# X = lose, 0pt
# Y = draw, 3pt
# Z = win, 6pt

score = 0

with open('rpc_strategy_guide.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row[1] == 'X':
            score = score + 0
        if row[1] == 'Y':
            score = score + 3
        if row[1] == 'Z':
            score = score + 6

        if row[1] == 'X' and row[0] == 'A':
            score = score + 3
        if row[1] == 'Y' and row[0] == 'A':
            score = score + 1
        if row[1] == 'Z' and row[0] == 'A':
            score = score + 2
        if row[1] == 'X' and row[0] == 'B':
            score = score + 1
        if row[1] == 'Y' and row[0] == 'B':
            score = score + 2
        if row[1] == 'Z' and row[0] == 'B':
            score = score + 3
        if row[1] == 'X' and row[0] == 'C':
            score = score + 2
        if row[1] == 'Y' and row[0] == 'C':
            score = score + 3
        if row[1] == 'Z' and row[0] == 'C':
            score = score + 1
        

print(score)
        






