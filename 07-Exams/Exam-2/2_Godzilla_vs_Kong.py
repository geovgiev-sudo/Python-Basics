budget = float(input())
extras = int(input())
clothing_per_extra = float(input())

dekor = budget * 0.10
clothing_price = clothing_per_extra * extras

if extras > 150:
    clothing_price *= 0.90

money_needed = dekor + clothing_price

if money_needed > budget:
    money_not_enough = money_needed - budget
    print(f'Not enough money!')
    print(f'Wingard needs {money_not_enough:.2f} leva more.')

else:
    money_left = budget - money_needed
    print(f'Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')