desired_income = float(input())
command = input()

cocktail_order = 0
income = 0

while command != 'Party!':
    cocktail_name = command
    number_of_cocktails = int(input())

    cocktail_price = len(cocktail_name)
    cocktail_order = number_of_cocktails * len(cocktail_name)

    if cocktail_order % 2 != 0:
        cocktail_order *= 0.75

    income += cocktail_order

    if income >= desired_income:
        print(f'Target acquired.')
        print(f'Club income - {income:.2f} leva.')
        break

    command = input()

else:
    money_needed = desired_income - income
    print(f'We need {money_needed:.2f} leva more.')
    print(f'Club income - {income:.2f} leva.')