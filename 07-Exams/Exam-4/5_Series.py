budget = float(input())
number_of_series = int(input())
price_total = 0

for i in range(1, number_of_series + 1):
    series_name = input()
    series_price = float(input())

    if series_name == 'Thrones':
        series_price *= 0.50
    elif series_name == 'Lucifer':
        series_price *= 0.60
    elif series_name == 'Protector':
        series_price *= 0.70
    elif series_name == 'TotalDrama':
        series_price *= 0.80
    elif series_name == 'Area':
        series_price *= 0.90

    price_total += series_price

if budget >= price_total:
    money_left = budget - price_total
    print(f'You bought all the series and left with {money_left:.2f} lv.')

elif budget < price_total:
    money_needed = price_total - budget
    print(f'You need {money_needed:.2f} lv. more to buy the series!')