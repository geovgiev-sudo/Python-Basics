budget = float(input())
litres_needed = float(input())
day_of_week = input()

price_litre_fuel = 2.10
price_guide = 100
price_safari = litres_needed * price_litre_fuel + price_guide
if day_of_week == 'Saturday':
    price_safari *= 0.90
elif day_of_week == 'Sunday':
    price_safari *= 0.80

if budget >= price_safari:
    money_left = budget - price_safari
    print(f'Safari time! Money left: {money_left:.2f} lv.')
elif budget < price_safari:
    money_needed = price_safari - budget
    print(f'Not enough money! Money needed: {money_needed:.2f} lv.')