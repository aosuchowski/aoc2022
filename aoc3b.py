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

elf_groups = list(zip(*[iter(df[0])] * 3))

def item_check(first_rucksack_item, second_rucksack):
    for i in range(len(second_rucksack)):
        if first_rucksack_item == second_rucksack[i]:
            return first_rucksack_item

def badge_check(first_same_item, third_rucksack):
    for i in range(len(third_rucksack)):
        if first_same_item == third_rucksack[i]:
            return items.get(third_rucksack[i])

priority = 0

for group in elf_groups:
    same_items = []
    rucksack_1 = group[0]
    rucksack_2 = group[1]
    rucksack_3 = group[2]

    for i in range(len(rucksack_1)):
        same_item = item_check(rucksack_1[i], rucksack_2)
        if same_item:
            same_items.append(same_item)
    same_items = list(set(same_items))

    for j in range(len(same_items)):
        item_priority_score = badge_check(same_items[j], rucksack_3)
        if item_priority_score:
            priority = priority + item_priority_score
            print(priority)
            print(list(items.keys())[list(items.values()).index(item_priority_score)])
            break

print(priority)
       


