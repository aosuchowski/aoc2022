import csv

stacks = {
    '1':['D', 'L', 'V', 'T', 'M', 'H', 'F',],
    '2':['H', 'Q', 'G', 'J', 'C', 'T', 'N', 'P',],
    '3':['R', 'S', 'D', 'M', 'P', 'H',],
    '4':['L', 'B', 'V', 'F',],
    '5':['N', 'H', 'G', 'L', 'Q',],
    '6':['W', 'B', 'D', 'G', 'R', 'M', 'P',],
    '7':['G', 'M', 'N', 'R', 'C', 'H', 'L','Q',],
    '8':['C', 'L', 'W',],
    '9':['R', 'D', 'L', 'Q', 'J', 'Z', 'M','T',],
}

with open('crate_moves.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        move = stacks[row[1]][-1*int(row[0]):]
        move = move[::-1]

        stacks[row[1]] = stacks[row[1]][:len(stacks[row[1]])-int(row[0])]

        new_stack = stacks[row[2]] + move
        stacks[row[2]] = new_stack

for i in list(stacks.keys()):
    print(stacks[i][-1])
    