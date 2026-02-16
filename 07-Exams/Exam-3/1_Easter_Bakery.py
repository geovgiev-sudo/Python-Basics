price_brashno_kg = float(input())
brashno_kg = float(input())
sugar_kg = float(input())
kori_eggs = int(input())
pakets_maya = int(input())

price_sugar_kg = price_brashno_kg * 0.75
price_kora_eggs = price_brashno_kg * 1.10
price_maya = price_sugar_kg * 0.20

brashno = price_brashno_kg * brashno_kg
sugar = price_sugar_kg * sugar_kg
eggs = price_kora_eggs * kori_eggs
maya = price_maya * pakets_maya

total = brashno + sugar + eggs + maya

print(f'{total:.2f}')