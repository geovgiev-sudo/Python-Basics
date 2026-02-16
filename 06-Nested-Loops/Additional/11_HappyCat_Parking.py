days = int(input())
hours_count = int(input())
price = 0
total_price = 0
price_today = 0

for day in range(1, days + 1):
    price_today = 0
    for hour in range(1, hours_count + 1):

        if day % 2 == 0 and hour % 2 != 0:
            price = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1

        price_today += price
    total_price += price_today

    print(f'Day: {day} - {price_today:.2f} leva')

print(f'Total: {total_price:.2f} leva')