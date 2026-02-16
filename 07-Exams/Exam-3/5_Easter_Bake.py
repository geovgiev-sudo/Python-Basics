import sys
from math import ceil
from sys import maxsize

kozunaks_count = int(input())
paket_sugar = 950
paket_flower = 750
sugar_needed = 0
flower_needed = 0
max_used_sugar = -sys.maxsize
max_used_flower = -sys.maxsize

for i in range(1, kozunaks_count + 1):
    sugar_grams = int(input())
    flower_grams = int(input())
    sugar_needed += sugar_grams
    flower_needed += flower_grams

    if max_used_sugar < sugar_grams:
        max_used_sugar = sugar_grams
    if max_used_flower < flower_grams:
        max_used_flower = flower_grams

paketi_sugar = ceil(sugar_needed / paket_sugar)
paketi_flower = ceil(flower_needed / paket_flower)

print(f'Sugar: {paketi_sugar}')
print(f'Flour: {paketi_flower}')
print(f'Max used flour is {max_used_flower} grams, max used sugar is {max_used_sugar} grams.')