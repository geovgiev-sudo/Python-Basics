dograma_count = int(input())
dograma_type = input()
delivery_type = input()
delivery_fee = 60
dograma_unit_price = 0
dograma_total = 0

if dograma_count < 10:
    print(f'Invalid order')

if dograma_type == '90X130':
    dograma_unit_price = 110
    dograma_total = dograma_count * dograma_unit_price
    if 30 < dograma_count <= 60:
        dograma_total *= 0.95
    elif 60 < dograma_count:
        dograma_total *= 0.92

elif dograma_type == '100X150':
    dograma_unit_price = 140
    dograma_total = dograma_count * dograma_unit_price
    if 40 < dograma_count <= 80:
        dograma_total *= 0.94
    elif 80 < dograma_count:
        dograma_total *= 0.90

elif dograma_type == '130X180':
    dograma_unit_price = 190
    dograma_total = dograma_count * dograma_unit_price
    if 20 < dograma_count <= 50:
        dograma_total *= 0.93
    elif 50 < dograma_count:
        dograma_total *= 0.88

elif dograma_type == '200X300':
    dograma_unit_price = 250
    dograma_total = dograma_count * dograma_unit_price
    if 25 < dograma_count <= 50:
        dograma_total *= 0.91
    elif 50 < dograma_count:
        dograma_total *= 0.86

if delivery_type == 'With delivery':
    dograma_total += delivery_fee

if dograma_count > 99:
    dograma_total *= 0.96

if dograma_count >= 10:
    print(f'{dograma_total:.2f} BGN')
