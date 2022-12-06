import urllib3
from bs4 import BeautifulSoup
import csv

# http = urllib3.PoolManager()
# url = 'https://adventofcode.com/2022/day/1/input'
# response = http.request('GET', url)
# soup = BeautifulSoup(response.data)

# for row in soup():
#     print(row)

elf_cal_inv = []
elf_cals = 0

with open('elf_calories.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if not row:
            elf_cal_inv.append(elf_cals)
            elf_cals = 0
            continue
        elf_cals = int(row[0]) + elf_cals
elf_cal_inv.append(elf_cals)

# Part 1
print(max(elf_cal_inv))

# Part 2
elf_cal_inv.sort(reverse=True)
print(sum(elf_cal_inv[0:3]))
