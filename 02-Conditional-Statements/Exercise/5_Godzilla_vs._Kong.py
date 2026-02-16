budget = float(input())
extras = int(input())
price_clothing = float(input())

decor = budget * 0.10
total_clothing = extras * price_clothing
if extras > 150:
    total_clothing *= 0.90
    # изчисляваме 10% отстъпка
    # total_clothing * 0.90
    # total_clothing - (total_clothing * 0.10)
    # total_clothing -= total_clothing * 0.10
budget_needed = total_clothing + decor
difference = abs(budget - budget_needed) # намираме абсолютната стойност - изчисляваме разликата между разходите и бюджета

if budget_needed > budget:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
elif budget_needed <= budget:
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')
