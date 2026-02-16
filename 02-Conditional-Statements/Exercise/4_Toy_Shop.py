puzzle = 2.60
doll = 3
bear = 4.10
mignon = 8.20
truck = 2

trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
mignons = int(input())
trucks = int(input())

total_price = ((puzzles * puzzle) + (dolls * doll) + (bears * bear) + (mignons * mignon) + (trucks * truck))
total_toys = puzzles + dolls + bears + mignons + trucks

if total_toys >= 50:
    total_price *= 0.75 # 25% отстъпка

rent = total_price * 0.10
profit = total_price - rent

difference = abs(profit - trip_price)
# Изчисляваме абсолютна стойност - тоест дори и profit < trip_price,
# като го извадим, пак ще получим положително число (абсолютната стойност).

if profit >= trip_price:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')