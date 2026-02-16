budget = float(input())
season = input()
place = ''
country = ''
price = 0

if 1000 >= budget:
    place = 'Camp'
    if season == 'Summer':
        country = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        country = 'Morocco'
        price = budget * 0.45

elif 1000 < budget <= 3000:
    place = 'Hut'
    if season == 'Summer':
        country = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        country = 'Morocco'
        price = budget * 0.60

elif 3000 < budget:
    place = 'Hotel'
    if season == 'Summer':
        country = 'Alaska'
        price = budget * 0.90
    elif season == 'Winter':
        country = 'Morocco'
        price = budget * 0.90

print(f'{country} - {place} - {price:.2f}')