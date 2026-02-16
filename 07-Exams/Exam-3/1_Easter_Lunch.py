kozunak_price = 3.20
kora_eggs_price = 4.35 # 1 kora e 12 eggs
kurabia_price = 5.40
boya_egg = 0.15

kozunatzi = int(input())
kori_eggs = int(input())
kurabii_kg = int(input())

kozunak = kozunak_price * kozunatzi
eggs = kora_eggs_price * kori_eggs
kurabia = kurabia_price * kurabii_kg
boya = kori_eggs * 12 * boya_egg

total = kozunak + eggs + kurabia + boya
print(f'{total:.2f}')