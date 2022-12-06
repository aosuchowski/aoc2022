import csv

fully_contained_pairs = 0

with open('cleaning_sections.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if int(row[2]) <= int(row[0]) <= int(row[3]):
            fully_contained_pairs = fully_contained_pairs + 1
            continue
        if int(row[2]) <= int(row[1]) <= int(row[3]):
            fully_contained_pairs = fully_contained_pairs + 1
            continue
        if int(row[0]) <= int(row[2]) <= int(row[1]):
            fully_contained_pairs = fully_contained_pairs + 1
            continue
        if int(row[0]) <= int(row[3]) <= int(row[1]):
            fully_contained_pairs = fully_contained_pairs + 1

print(fully_contained_pairs)


