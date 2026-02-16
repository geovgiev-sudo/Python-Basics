inherited_money = float(input())
year_to_live = int(input())

starting_year = 1800
age = 17
money_spent = 0

for year in range(starting_year, year_to_live + 1):
    age = age + 1
    if year % 2 == 0:
        money_spent += 12000
    elif year % 2 == 1:
        money_spent += 12000 + 50 * age

if inherited_money >= money_spent:
    money_left = inherited_money - money_spent
    print(f'Yes! He will live a carefree life and will have {money_left:.2f} dollars left.')
else:
    money_needed = abs(inherited_money - money_spent)
    print(f'He will need {money_needed:.2f} dollars to survive.')