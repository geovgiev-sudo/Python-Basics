distance = int(input())
day_night = str(input())

taxi_day = 0.7 + distance * 0.79
taxi_night = 0.7 + distance * 0.90

bus = distance * 0.09
train = distance * 0.06

if day_night == 'day':
    if distance < 20:
        print(f'{taxi_day:.2f}')
    elif distance < 100:
        print(f'{bus:.2f}')
    else:
        print(f'{train:.2f}')
else:
    if distance < 20:
        print(f'{taxi_night:.2f}')
    elif distance < 100:
        print(f'{bus:.2f}')
    else:
        print(f'{train:.2f}')


n = int(input())
when = input()

taxi_start = 0.70
taxi_day = 0.79
taxi_night = 0.90
bus_tariff = 0.09
train_tariff = 0.06
# tariff = taxi_day if when == 'day' else taxi_night
if n < 20:
    if when == 'day':
        price = taxi_start + n * taxi_day
        print(f'{price:.2f}')
    elif when == 'night':
        price = taxi_start + n * taxi_night
        print(f'{price:.2f}')
elif 20 <= n < 100:
    price = n * bus_tariff
    print(f'{price:.2f}')
elif 100 <= n:
    price = n * train_tariff
    print(f'{price:.2f}')