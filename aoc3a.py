import pandas as pd

items = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26,
    "A":27,
    "B":28,
    "C":29,
    "D":30,
    "E":31,
    "F":32,
    "G":33,
    "H":34,
    "I":35,
    "J":36,
    "K":37,
    "L":38,
    "M":39,
    "N":40,
    "O":41,
    "P":42,
    "Q":43,
    "R":44,
    "S":45,
    "T":46,
    "U":47,
    "V":48,
    "W":49,
    "X":50,
    "Y":51,
    "Z":52,
}

df = pd.read_csv('rucksack_items.csv', header=None)

priority = 0

def item_check(first_compartment_item, second_compartment):
    for i in range(len(second_compartment)):
        if first_compartment_item == second_compartment[i]:
            return items.get(second_compartment[i])

for i in df[0]:
    first_compartment, second_compartment = i[:len(i)//2], i[len(i)//2:]
    for j in range(len(first_compartment)):
        item_priority_score = item_check(first_compartment[j], second_compartment)
        if type(item_priority_score) == int:
            priority = priority + item_priority_score
            break

print(priority)
