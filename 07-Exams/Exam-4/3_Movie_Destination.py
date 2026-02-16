film_budget = float(input())
destination = input()
season = input()
days_count = int(input())
day_price = 0
end_price = 0

if destination == 'Dubai':
    if season == 'Winter':
        day_price = 45000
    elif season == 'Summer':
        day_price = 40000

    end_price = (day_price * days_count) * 0.70

elif destination == 'Sofia':
    if season == 'Winter':
        day_price = 17000
    elif season == 'Summer':
        day_price = 12500

    end_price = (day_price * days_count) * 1.25

elif destination == 'London':
    if season == 'Winter':
        day_price = 24000
    elif season == 'Summer':
        day_price = 20250

    end_price = (day_price * days_count)

if film_budget >= end_price:
    money_left = film_budget - end_price
    print(f'The budget for the movie is enough! We have {money_left:.2f} leva left!')

elif film_budget < end_price:
    money_needed = end_price - film_budget
    print(f'The director needs {money_needed:.2f} leva more!')