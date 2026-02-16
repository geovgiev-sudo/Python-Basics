film = input()
paket = input()
tickets_count = int(input())
price = 0
total_sum = 0

if film == 'John Wick':
    if paket == 'Drink':
        price = 12
    elif paket == 'Popcorn':
        price = 15
    elif paket == 'Menu':
        price = 19
    total_sum = tickets_count * price

elif film == 'Star Wars':
    if paket == 'Drink':
        price = 18
    elif paket == 'Popcorn':
        price = 25
    elif paket == 'Menu':
        price = 30
    total_sum = tickets_count * price
    if tickets_count >= 4:
        total_sum *= 0.70

elif film == 'Jumanji':
    if paket == 'Drink':
        price = 9
    elif paket == 'Popcorn':
        price = 11
    elif paket == 'Menu':
        price = 14
    total_sum = tickets_count * price
    if tickets_count == 2:
        discount = total_sum * 0.15
        total_sum = total_sum - discount

print(f'Your bill is {total_sum:.2f} leva.')