screening_type = input()
r = int(input())
c = int(input())
price = 0.0
total = 0.0

if screening_type == 'Premiere':
    price = 12
    total = r * c * price
elif screening_type == 'Normal':
    price = 7.50
    total = r * c * price
elif screening_type == 'Discount':
    price = 5
    total = r * c * price

print(f'{total:.2f} leva')