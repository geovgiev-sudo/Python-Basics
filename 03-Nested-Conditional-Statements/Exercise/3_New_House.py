flower_type = input()
flowers_count = int(input())
budget = int(input())

rose = 5
dahlia = 3.80
tulip = 2.80
narcissus = 3
gladiolus = 2.50

price = 0.0

if flower_type == 'Roses':
    price = flowers_count * rose
    if flowers_count > 80:
        price *= 0.90

elif flower_type == 'Dahlias':
    price = flowers_count * dahlia
    if flowers_count > 90:
        price *= 0.85

elif flower_type == 'Tulips':
    price = flowers_count * tulip
    if flowers_count > 80:
        price *= 0.85

elif flower_type == 'Narcissus':
    price = flowers_count * narcissus
    if flowers_count < 120:
        price *= 1.15

elif flower_type == 'Gladiolus':
    price = flowers_count * gladiolus
    if flowers_count < 80:
        price *= 1.20

difference_between_price_and_budget = abs(budget - price)

if budget >= price:
    print(f'Hey, you have a great garden with {flowers_count} {flower_type} '
          f'and {difference_between_price_and_budget:.2f} leva left.')
elif budget < price:
    print(f'Not enough money, you need {difference_between_price_and_budget:.2f} leva more.')


