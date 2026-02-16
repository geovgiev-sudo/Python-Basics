from math import ceil

kozunak_price = 4
egg_price = 0.45

guests = int(input())
budget = int(input())

kozunak_needed = ceil(guests / 3)
eggs_needed = guests * 2

kozunak = kozunak_price * kozunak_needed
eggs = eggs_needed * egg_price
total = kozunak + eggs

if total <= budget:
    money_left = budget - total
    print(f'Lyubo bought {kozunak_needed} Easter bread and {eggs_needed} eggs.')
    print(f'He has {money_left:.2f} lv. left.')

else:
    money_needed = total - budget
    print(f'Lyubo doesn\'t have enough money.')
    print(f'He needs {money_needed:.2f} lv. more.')